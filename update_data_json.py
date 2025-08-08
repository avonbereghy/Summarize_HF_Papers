#!/usr/bin/env python3
"""
Script to update data.json with all available paper summaries.
Run this after adding new papers to automatically update the website data.
"""

import json
import os
from pathlib import Path
from datetime import datetime

def scan_papers_directory():
    """Scan the repository for all paper directories and their summaries."""
    papers_data = {}
    
    # Check both old structure (for backward compatibility) and new structure
    base_paths = [Path('.'), Path('papers_archive')]
    
    for base_path in base_paths:
        if not base_path.exists():
            continue
            
        # Find all papers_YYYY-MM-DD directories
        for papers_dir in base_path.glob('papers_*'):
            if papers_dir.is_dir():
                # Extract date from directory name (papers_YYYY-MM-DD)
                date_str = papers_dir.name.replace('papers_', '')
                
                # Skip if we already have this date (from higher priority path)
                if date_str in papers_data:
                    continue
                
                # Find all paper subdirectories
                paper_entries = []
                for paper_dir in sorted(papers_dir.iterdir()):
                    if paper_dir.is_dir():
                        paper_id = paper_dir.name
                        
                        # Check if summary.md and metadata.json exist
                        summary_path = paper_dir / 'summary.md'
                        metadata_path = paper_dir / 'metadata.json'
                        
                        if summary_path.exists() and metadata_path.exists():
                            paper_entries.append({
                                'id': paper_id,
                                'path': str(paper_dir).replace('\\', '/')  # Ensure forward slashes
                            })
                
                if paper_entries:
                    papers_data[date_str] = paper_entries
    
    return papers_data

def update_data_json():
    """Update the data.json file with current paper information."""
    papers_data = scan_papers_directory()
    
    # Sort by date (newest first for display purposes)
    sorted_papers = dict(sorted(papers_data.items(), reverse=True))
    
    data = {
        'papers': sorted_papers,
        'last_updated': datetime.now().isoformat()
    }
    
    # Write to data.json
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Updated data.json with {len(sorted_papers)} dates containing papers:")
    for date, papers in sorted_papers.items():
        print(f"  - {date}: {len(papers)} papers")

if __name__ == '__main__':
    update_data_json()