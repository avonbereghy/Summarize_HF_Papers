#!/usr/bin/env python3
"""
Scrape Hugging Face papers and summarize them using Gemini
"""

import os
import requests
from datetime import datetime
import time
from pathlib import Path
from bs4 import BeautifulSoup
import json
from langchain.chat_models.base import init_chat_model

def get_model():
    """Initialize Gemini model using provided configuration"""
    try:
        # First try with Gemini API key from environment
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if api_key:
            return init_chat_model(
                model="gemini-1.5-flash",
                model_provider="google-genai",
                temperature=0.3,
                api_key=api_key
            )
        else:
            raise ValueError("No Gemini API key found in environment variables")
    except Exception as e:
        print(f"Error initializing Gemini model: {e}")
        print("Please set GEMINI_API_KEY or GOOGLE_API_KEY environment variable")
        return None

def fetch_papers_list(date_str=None):
    """Fetch list of papers from Hugging Face for a specific date"""
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Try the date-specific page
    page_url = f"https://huggingface.co/papers/date/{date_str}"
    
    try:
        response = requests.get(page_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response.raise_for_status()
        
        # Parse the HTML to extract paper information
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        papers = []
        # Look for paper links in the page
        for link in soup.find_all('a', href=True):
            href = link['href']
            if '/papers/' in href and href.count('/') == 2:
                paper_id = href.split('/papers/')[-1]
                # Remove any anchor tags (like #community)
                if '#' in paper_id:
                    paper_id = paper_id.split('#')[0]
                if paper_id and '.' in paper_id:  # Valid arxiv ID format
                    papers.append(paper_id)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_papers = []
        for paper_id in papers:
            if paper_id not in seen:
                seen.add(paper_id)
                unique_papers.append(paper_id)
        
        if unique_papers:
            return fetch_paper_details(unique_papers)
        else:
            print(f"No papers found for date {date_str}, trying API fallback...")
            return fetch_papers_api_fallback()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching papers list: {e}")
        return fetch_papers_api_fallback()

def fetch_paper_details(paper_ids):
    """Fetch details for a list of paper IDs"""
    papers = []
    for paper_id in paper_ids:
        paper_url = f"https://huggingface.co/papers/{paper_id}"
        api_url = f"https://huggingface.co/api/papers/{paper_id}"
        
        try:
            response = requests.get(api_url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            if response.status_code == 200:
                data = response.json()
                papers.append({
                    'id': paper_id,
                    'title': data.get('title', 'Unknown Title'),
                    'authors': data.get('authors', []),
                    'abstract': data.get('summary', ''),
                    'url': paper_url,
                    'pdf_url': f"https://arxiv.org/pdf/{paper_id}.pdf"
                })
            else:
                # If API fails, construct basic info
                papers.append({
                    'id': paper_id,
                    'title': f"Paper {paper_id}",
                    'authors': [],
                    'abstract': '',
                    'url': paper_url,
                    'pdf_url': f"https://arxiv.org/pdf/{paper_id}.pdf"
                })
        except Exception as e:
            print(f"Error fetching details for {paper_id}: {e}")
            papers.append({
                'id': paper_id,
                'title': f"Paper {paper_id}",
                'authors': [],
                'abstract': '',
                'url': paper_url,
                'pdf_url': f"https://arxiv.org/pdf/{paper_id}.pdf"
            })
    
    return papers

def fetch_papers_api_fallback():
    """Fallback to try the API endpoint"""
    api_url = "https://huggingface.co/api/daily-papers"
    
    try:
        response = requests.get(api_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API fallback also failed: {e}")
        # Final fallback to hardcoded papers
        return fetch_papers_fallback()

def fetch_papers_fallback():
    """Fallback method to get paper information"""
    # Known paper IDs from the 2025-08-07 page
    paper_ids = [
        "2508.04026",  # VeriGUI
        "2508.01191",  # Chain-of-Thought
        "2508.02694",  # Efficient Agents
        "2508.04700",  # SEAgent
        "2508.03501",  # Training Long-Context Agents
    ]
    
    return fetch_paper_details(paper_ids)

def download_paper_pdf(pdf_url, save_path):
    """Download PDF from given URL"""
    try:
        response = requests.get(pdf_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }, timeout=30)
        response.raise_for_status()
        
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"  ⚠️ Error downloading PDF: {e}")
        return False

def summarize_paper_with_gemini(paper_info, pdf_path=None):
    """Generate paper summary using Gemini"""
    model = get_model()
    
    # Create a prompt for summarization with enhanced formatting
    prompt = f"""
    Please provide a comprehensive summary of this academic paper using markdown formatting with **bold** and *italics* for emphasis:
    
    Title: {paper_info.get('title', 'Unknown')}
    Authors: {', '.join([author.get('name', '') if isinstance(author, dict) else str(author) for author in paper_info.get('authors', [])])}
    
    Abstract: {paper_info.get('abstract', 'Not available')}
    
    Please provide:
    
    ## Executive Summary
    Write a one-paragraph executive summary using **bold** for key concepts and *italics* for technical terms or emphasis.
    
    ## Key Contributions and Findings
    List 3-5 bullet points with **bold** headings for each contribution, followed by a brief explanation. Use *italics* for important details.
    
    ## Methodology Overview
    Briefly describe the methodology using **bold** for major components and *italics* for specific techniques.
    
    ## Results and Performance
    Summarize the key results with **bold** for metrics and *italics* for comparisons.
    
    ## Limitations and Future Work
    List any limitations mentioned and potential future directions.
    
    ## Practical Applications
    Describe potential real-world applications or implications.
    
    Format your response with proper markdown, using **bold** and *italics* throughout for emphasis and clarity.
    """
    
    try:
        response = model.invoke(prompt)
        return response.content
    except Exception as e:
        print(f"Error summarizing with Gemini: {e}")
        return f"Summary generation failed: {str(e)}"

def main():
    """Main function to orchestrate scraping and summarization"""
    # Create folder with today's date
    today = datetime.now().strftime("%Y-%m-%d")
    output_dir = Path(f"papers_{today}")
    output_dir.mkdir(exist_ok=True)
    
    print(f"📁 Created output directory: {output_dir}")
    
    # Fetch papers - pass the date to fetch papers for today
    print("🔍 Fetching papers from Hugging Face...")
    papers = fetch_papers_list(today)
    
    if isinstance(papers, dict):
        # If we got the daily papers response, extract the papers list
        papers = papers.get('papers', [])
    
    if not papers:
        print("⚠️ No papers found. Using fallback method...")
        papers = fetch_papers_fallback()
    
    print(f"📄 Found {len(papers)} papers to process")
    
    # Process each paper
    summaries = []
    for i, paper in enumerate(papers, 1):
        paper_id = paper.get('id', f'paper_{i}')
        title = paper.get('title', 'Unknown Title')
        
        print(f"\n[{i}/{len(papers)}] Processing: {title}")
        
        # Create paper directory
        paper_dir = output_dir / f"{paper_id.replace('/', '_')}"
        paper_dir.mkdir(exist_ok=True)
        
        # Try to download PDF
        pdf_path = paper_dir / f"{paper_id.replace('/', '_')}.pdf"
        pdf_url = paper.get('pdf_url', f"https://arxiv.org/pdf/{paper_id}.pdf")
        
        print(f"  📥 Downloading PDF...")
        pdf_downloaded = download_paper_pdf(pdf_url, pdf_path)
        
        if not pdf_downloaded:
            print(f"  ⚠️ Could not download PDF, using abstract only")
        
        # Generate summary with Gemini
        print(f"  🤖 Generating summary with Gemini...")
        summary = summarize_paper_with_gemini(paper, pdf_path if pdf_downloaded else None)
        
        # Save summary
        summary_path = paper_dir / "summary.md"
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"**Paper ID:** {paper_id}\n\n")
            f.write(f"**Authors:** {', '.join([author.get('name', '') if isinstance(author, dict) else str(author) for author in paper.get('authors', ['Not available'])])}\n\n")
            f.write(f"**URL:** {paper.get('url', 'Not available')}\n\n")
            f.write("## Summary\n\n")
            f.write(summary)
        
        # Save paper metadata
        metadata_path = paper_dir / "metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(paper, f, indent=2)
        
        summaries.append({
            'title': title,
            'id': paper_id,
            'summary': summary,
            'pdf_downloaded': pdf_downloaded
        })
        
        print(f"  ✅ Saved summary to {summary_path}")
        
        # Rate limiting to be nice to APIs
        time.sleep(2)
    
    # Create master summary file
    master_summary_path = output_dir / "all_summaries.md"
    with open(master_summary_path, 'w', encoding='utf-8') as f:
        f.write(f"# Hugging Face Papers Summary - {today}\n\n")
        f.write(f"Total papers processed: {len(summaries)}\n\n")
        
        for item in summaries:
            f.write(f"## {item['title']}\n\n")
            f.write(f"**Paper ID:** {item['id']}\n")
            f.write(f"**PDF Downloaded:** {'Yes' if item['pdf_downloaded'] else 'No'}\n\n")
            f.write(item['summary'])
            f.write("\n\n---\n\n")
    
    print(f"\n✨ Processing complete!")
    print(f"📂 All papers saved in: {output_dir}/")
    print(f"📄 Master summary available at: {master_summary_path}")
    print(f"\n📈 Summary:")
    print(f"  - Total papers processed: {len(summaries)}")
    print(f"  - PDFs downloaded: {sum(1 for s in summaries if s['pdf_downloaded'])}")
    print(f"  - Summaries generated: {len(summaries)}")

if __name__ == "__main__":
    main()