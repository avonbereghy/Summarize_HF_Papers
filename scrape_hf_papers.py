#!/usr/bin/env python3
"""
Scrape Hugging Face papers and summarize them using AI models (Together AI Llama or Gemini)

Usage:
    # Use Together AI Meta Llama 3.3 70B (requires TOGETHER_API_KEY)
    python scrape_hf_papers.py --model together

    # Use Google Gemini (requires GEMINI_API_KEY or GOOGLE_API_KEY)
    python scrape_hf_papers.py --model gemini
    
    # Auto-detect model based on available API keys (default)
    python scrape_hf_papers.py --model auto
    
    # Fetch papers for a specific date
    python scrape_hf_papers.py --date 2024-08-07
    
    # Fetch papers for today
    python scrape_hf_papers.py --today
    
    # Fetch papers for a date range
    python scrape_hf_papers.py --start-date 2024-08-01 --end-date 2024-08-07
"""

import os
import requests
from datetime import datetime, timedelta
import time
from pathlib import Path
from bs4 import BeautifulSoup
import json
from langchain.chat_models.base import init_chat_model
import random
import argparse

def get_model(model_preference=None):
    """Initialize AI model using provided configuration"""
    try:
        # If user specified a preference, try that first
        if model_preference == "together":
            together_api_key = os.getenv("TOGETHER_API_KEY")
            if together_api_key:
                print("🤖 Using Together AI Meta Llama 3.3 70B Instruct Turbo")
                return init_chat_model(
                    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
                    model_provider="together",
                    temperature=0.3,
                    api_key=together_api_key
                )
            else:
                raise ValueError("TOGETHER_API_KEY environment variable not found")
        
        elif model_preference == "gemini":
            gemini_api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
            if gemini_api_key:
                print("🤖 Using Google Gemini 1.5 Flash")
                return init_chat_model(
                    model="gemini-1.5-flash",
                    model_provider="google-genai",
                    temperature=0.3,
                    api_key=gemini_api_key
                )
            else:
                raise ValueError("GEMINI_API_KEY or GOOGLE_API_KEY environment variable not found")
        
        # Auto-detect based on available API keys
        together_api_key = os.getenv("TOGETHER_API_KEY")
        if together_api_key:
            print("🤖 Using Together AI Meta Llama 3.3 70B Instruct Turbo")
            return init_chat_model(
                model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
                model_provider="together",
                temperature=0.3,
                api_key=together_api_key
            )
        
        # Fallback to Gemini
        gemini_api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if gemini_api_key:
            print("🤖 Using Google Gemini 1.5 Flash")
            return init_chat_model(
                model="gemini-1.5-flash",
                model_provider="google-genai",
                temperature=0.3,
                api_key=gemini_api_key
            )
        else:
            raise ValueError("No API key found. Please set TOGETHER_API_KEY or GEMINI_API_KEY/GOOGLE_API_KEY environment variable")
    except Exception as e:
        print(f"Error initializing AI model: {e}")
        print("Please set TOGETHER_API_KEY or GEMINI_API_KEY/GOOGLE_API_KEY environment variable")
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
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for paper links
        papers = []
        paper_elements = soup.find_all('article')
        
        for element in paper_elements:
            # Extract paper ID from link
            link_elem = element.find('a', href=True)
            if link_elem and '/papers/' in link_elem['href']:
                paper_id = link_elem['href'].split('/papers/')[-1]
                
                # Extract title
                title_elem = element.find('h3')
                title = title_elem.text.strip() if title_elem else paper_id
                
                # Extract abstract (if available)
                abstract_elem = element.find('p')
                abstract = abstract_elem.text.strip() if abstract_elem else ""
                
                papers.append({
                    'id': paper_id,
                    'title': title,
                    'abstract': abstract,
                    'url': f"https://huggingface.co/papers/{paper_id}",
                    'pdf_url': f"https://arxiv.org/pdf/{paper_id}.pdf"
                })
        
        # If we found papers, fetch detailed info
        if papers:
            print(f"Found {len(papers)} papers on the page")
            return fetch_paper_details([p['id'] for p in papers])
        else:
            print("No papers found on the page, trying API...")
            return fetch_papers_api()
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching papers page: {e}")
        return fetch_papers_api()

def fetch_paper_details(paper_ids):
    """Fetch detailed information about papers"""
    papers = []
    
    for paper_id in paper_ids[:6]:  # Limit to first 6 papers
        try:
            # Fetch from Hugging Face API
            api_url = f"https://huggingface.co/api/papers/{paper_id}"
            response = requests.get(api_url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            
            if response.status_code == 200:
                paper_data = response.json()
                papers.append({
                    'id': paper_id,
                    'title': paper_data.get('title', ''),
                    'abstract': paper_data.get('summary', ''),
                    'authors': paper_data.get('authors', []),
                    'url': f"https://huggingface.co/papers/{paper_id}",
                    'pdf_url': f"https://arxiv.org/pdf/{paper_id}.pdf"
                })
            else:
                # Fallback to basic info
                papers.append({
                    'id': paper_id,
                    'title': paper_id,
                    'abstract': 'Not available',
                    'authors': [],
                    'url': f"https://huggingface.co/papers/{paper_id}",
                    'pdf_url': f"https://arxiv.org/pdf/{paper_id}.pdf"
                })
                
        except Exception as e:
            print(f"Error fetching details for paper {paper_id}: {e}")
            continue
    
    return papers

def fetch_papers_api():
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

def summarize_paper_with_ai(paper_info, pdf_path=None, max_retries=5, model_preference=None):
    """Generate paper summary using AI model with rate limit handling"""
    model = get_model(model_preference)
    
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
    
    for attempt in range(max_retries):
        try:
            response = model.invoke(prompt)
            return response.content
        except Exception as e:
            error_str = str(e)
            
            # Check if this is a rate limit error
            if "429" in error_str or "quota" in error_str.lower() or "rate" in error_str.lower():
                if attempt < max_retries - 1:
                    # Calculate exponential backoff with jitter
                    base_delay = 2 ** attempt  # 1, 2, 4, 8, 16 seconds
                    jitter = random.uniform(0.5, 1.5)  # Add randomness to avoid thundering herd
                    delay = base_delay * jitter
                    
                    print(f"  ⏱️ Rate limit hit. Waiting {delay:.1f} seconds before retry {attempt + 1}/{max_retries}...")
                    time.sleep(delay)
                    continue
                else:
                    print(f"  ❌ Rate limit exceeded after {max_retries} attempts. Skipping this paper.")
                    return f"Rate limit exceeded after {max_retries} attempts. Please try again later or increase your API quota."
            else:
                # For non-rate-limit errors, don't retry
                print(f"Error summarizing with AI model: {e}")
                return f"Summary generation failed: {str(e)}"
    
    return "Unexpected error in retry loop"

def load_progress(output_dir):
    """Load progress from previous run"""
    progress_file = output_dir / ".progress.json"
    if progress_file.exists():
        try:
            with open(progress_file, 'r') as f:
                return json.load(f)
        except:
            return {"completed_papers": [], "last_index": 0}
    return {"completed_papers": [], "last_index": 0}

def save_progress(output_dir, completed_papers, last_index):
    """Save current progress"""
    progress_file = output_dir / ".progress.json"
    progress = {
        "completed_papers": completed_papers,
        "last_index": last_index,
        "timestamp": datetime.now().isoformat()
    }
    with open(progress_file, 'w') as f:
        json.dump(progress, f, indent=2)

def process_single_date(target_date, model_preference):
    """Process papers for a single date"""
    # Create folder within papers_archive directory
    output_dir = Path(f"papers_archive/papers_{target_date}")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"📁 Created output directory: {output_dir}")
    
    # Load previous progress if exists
    progress = load_progress(output_dir)
    completed_paper_ids = set(progress.get("completed_papers", []))
    last_index = progress.get("last_index", 0)
    
    if completed_paper_ids:
        print(f"📄 Resuming from previous run. {len(completed_paper_ids)} papers already completed.")
    
    # Fetch papers - pass the date to fetch papers for target date
    print("🔍 Fetching papers from Hugging Face...")
    papers = fetch_papers_list(target_date)
    
    if isinstance(papers, dict):
        # If we got the daily papers response, extract the papers list
        papers = papers.get('papers', [])
    
    if not papers:
        print("⚠️ No papers found. Using fallback method...")
        papers = fetch_papers_fallback()
    
    print(f"📄 Found {len(papers)} papers to process")
    
    # Limit to first 6 papers
    papers = papers[:6]
    print(f"📄 Processing first {len(papers)} papers")
    
    # Filter out already completed papers
    remaining_papers = []
    for paper in papers:
        paper_id = paper.get('id', '')
        if paper_id not in completed_paper_ids:
            remaining_papers.append(paper)
    
    if not remaining_papers:
        print("✅ All papers already processed!")
        return
        
    print(f"📄 {len(remaining_papers)} papers remaining to process")
    
    # Process each paper
    summaries = []
    start_index = len(papers) - len(remaining_papers)
    
    for i, paper in enumerate(remaining_papers):
        current_index = start_index + i + 1
        paper_id = paper.get('id', f'paper_{current_index}')
        title = paper.get('title', 'Unknown Title')
        
        print(f"\n[{current_index}/{len(papers)}] Processing: {title}")
        
        # Create paper directory
        paper_dir = output_dir / f"{paper_id.replace('/', '_')}"
        paper_dir.mkdir(exist_ok=True)
        
        # Check if summary already exists
        summary_path = paper_dir / "summary.md"
        if summary_path.exists():
            print(f"  ✅ Summary already exists, skipping...")
            completed_paper_ids.add(paper_id)
            save_progress(output_dir, list(completed_paper_ids), current_index)
            continue
        
        try:
            # Try to download PDF
            pdf_path = paper_dir / f"{paper_id.replace('/', '_')}.pdf"
            pdf_url = paper.get('pdf_url', f"https://arxiv.org/pdf/{paper_id}.pdf")
            
            print(f"  📥 Downloading PDF...")
            pdf_downloaded = download_paper_pdf(pdf_url, pdf_path)
            
            if not pdf_downloaded:
                print(f"  ⚠️ Could not download PDF, using abstract only")
            
            # Generate summary with AI model
            print(f"  🤖 Generating summary with AI model...")
            summary = summarize_paper_with_ai(paper, pdf_path if pdf_downloaded else None, model_preference=model_preference)
            
            # Check if summary generation was successful
            if "Rate limit exceeded" in summary:
                print(f"  ⏸️ Rate limit hit. Saving progress and stopping.")
                save_progress(output_dir, list(completed_paper_ids), current_index - 1)
                print(f"  💾 Progress saved. Run the script again to continue from where you left off.")
                return
            
            # Save summary
            authors_list = ', '.join([author.get('name', '') if isinstance(author, dict) else str(author) for author in paper.get('authors', ['Not available'])])
            with open(summary_path, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"**Paper ID:** {paper_id}\n\n")
                f.write(f"**URL:** {paper.get('url', 'Not available')}\n\n")
                f.write("## Summary\n\n")
                f.write(summary)
                f.write(f"\n\n---\n\n**Authors:** {authors_list}\n")
            
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
            
            # Mark as completed and save progress
            completed_paper_ids.add(paper_id)
            save_progress(output_dir, list(completed_paper_ids), current_index)
            
            # Rate limiting to be nice to APIs
            time.sleep(2)
            
        except KeyboardInterrupt:
            print(f"\n⏸️ Processing interrupted by user. Saving progress...")
            save_progress(output_dir, list(completed_paper_ids), current_index - 1)
            print(f"💾 Progress saved. Run the script again to continue from where you left off.")
            return
        except Exception as e:
            print(f"  ❌ Error processing paper {paper_id}: {e}")
            print(f"  ⏭️ Skipping to next paper...")
            continue
    
    # Create master summary file
    master_summary_path = output_dir / "all_summaries.md"
    with open(master_summary_path, 'w', encoding='utf-8') as f:
        f.write(f"# Hugging Face Papers Summary - {target_date}\n\n")
        f.write(f"Total papers processed: {len(summaries)}\n\n")
        
        for item in summaries:
            f.write(f"## {item['title']}\n\n")
            f.write(f"**Paper ID:** {item['id']}\n")
            f.write(f"**PDF Downloaded:** {'Yes' if item['pdf_downloaded'] else 'No'}\n\n")
            f.write(item['summary'])
            f.write("\n\n---\n\n")
    
    print(f"\n✨ Processing complete for {target_date}!")
    print(f"📂 All papers saved in: {output_dir}/")
    print(f"📄 Master summary available at: {master_summary_path}")
    print(f"\n📈 Summary:")
    print(f"  - Total papers processed: {len(summaries)}")
    print(f"  - PDFs downloaded: {sum(1 for s in summaries if s['pdf_downloaded'])}")
    print(f"  - Summaries generated: {len(summaries)}")

def main():
    """Main function to orchestrate scraping and summarization"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Scrape HuggingFace papers and generate AI summaries')
    parser.add_argument('--model', choices=['together', 'gemini', 'auto'], default='auto',
                        help='AI model to use: together (Meta Llama 3.3 70B), gemini (Gemini 1.5 Flash), or auto (detect based on available API keys)')
    parser.add_argument('--date', type=str, default=None,
                        help='Date to fetch papers for (YYYY-MM-DD format). Defaults to today.')
    parser.add_argument('--start-date', type=str, default=None,
                        help='Start date for range processing (YYYY-MM-DD format)')
    parser.add_argument('--end-date', type=str, default=None,
                        help='End date for range processing (YYYY-MM-DD format)')
    parser.add_argument('--today', action='store_true',
                        help='Process today\'s papers')
    args = parser.parse_args()
    
    # Determine which dates to process
    dates_to_process = []
    
    if args.today:
        dates_to_process = [datetime.now().strftime("%Y-%m-%d")]
    elif args.start_date and args.end_date:
        # Process date range
        current_date = datetime.strptime(args.start_date, "%Y-%m-%d")
        end_date = datetime.strptime(args.end_date, "%Y-%m-%d")
        while current_date <= end_date:
            dates_to_process.append(current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)
    elif args.date:
        # Process single specified date
        dates_to_process = [args.date]
    else:
        # Default to today
        dates_to_process = [datetime.now().strftime("%Y-%m-%d")]
    
    # Determine model preference
    model_preference = None if args.model == 'auto' else args.model
    
    # Process each date
    for idx, target_date in enumerate(dates_to_process, 1):
        if len(dates_to_process) > 1:
            print(f"\n{'='*60}")
            print(f"Processing date {idx}/{len(dates_to_process)}: {target_date}")
            print(f"{'='*60}\n")
        
        process_single_date(target_date, model_preference)
        
        # Pause between dates when processing multiple dates
        if len(dates_to_process) > 1 and idx < len(dates_to_process):
            print(f"\n⏸️ Pausing for 1 minute before next date...")
            time.sleep(60)
    
    if len(dates_to_process) > 1:
        print(f"\n🎉 All dates processed successfully!")
        print(f"📁 All summaries saved in: papers_archive/")

if __name__ == "__main__":
    main()