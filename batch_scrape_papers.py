#!/usr/bin/env python3
"""
Batch script to scrape HuggingFace papers for multiple dates
Runs scrape_hf_papers.py for each date from July 1, 2025 to August 6, 2025
"""

import subprocess
import time
from datetime import datetime, timedelta
import sys

def generate_date_range(start_date, end_date):
    """Generate a list of dates between start_date and end_date (inclusive)"""
    dates = []
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    
    while current_date <= end_date_obj:
        dates.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)
    
    return dates

def run_scraper_for_date(date_str, model="auto"):
    """Run the scraper script for a specific date"""
    cmd = [
        sys.executable, 
        "scrape_hf_papers.py",
        "--date", date_str,
        "--model", model
    ]
    
    print(f"\n🚀 Starting scraper for date: {date_str}")
    print(f"📝 Command: {' '.join(cmd)}")
    
    try:
        # Run the scraper script
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)  # 1 hour timeout
        
        if result.returncode == 0:
            print(f"✅ Successfully completed scraping for {date_str}")
            if result.stdout:
                print("📋 Output:")
                print(result.stdout)
        else:
            print(f"❌ Error scraping {date_str} (exit code: {result.returncode})")
            if result.stderr:
                print("💥 Error output:")
                print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print(f"⏰ Timeout: Scraping for {date_str} took longer than 1 hour")
        return False
    except Exception as e:
        print(f"💥 Exception while scraping {date_str}: {e}")
        return False
    
    return True

def main():
    """Main batch processing function"""
    # Date range: July 1, 2025 to August 6, 2025
    start_date = "2025-07-01"
    end_date = "2025-08-06"
    
    # Generate list of dates
    dates_to_process = generate_date_range(start_date, end_date)
    
    print(f"🎯 Batch Processing HuggingFace Papers")
    print(f"📅 Date range: {start_date} to {end_date}")
    print(f"📊 Total dates to process: {len(dates_to_process)}")
    print(f"⏱️  Estimated time: ~{len(dates_to_process) * 3} minutes (2 min pause between dates)")
    
    # Ask for confirmation
    response = input("\n🤔 Do you want to proceed? (y/N): ").strip().lower()
    if response not in ['y', 'yes']:
        print("❌ Batch processing cancelled.")
        return
    
    # Process each date
    successful_dates = []
    failed_dates = []
    
    for i, date_str in enumerate(dates_to_process, 1):
        print(f"\n📆 Processing date {i}/{len(dates_to_process)}: {date_str}")
        
        success = run_scraper_for_date(date_str)
        
        if success:
            successful_dates.append(date_str)
        else:
            failed_dates.append(date_str)
            
        # Pause between dates (except after the last one)
        if i < len(dates_to_process):
            print(f"⏸️  Pausing for 2 minutes before next date...")
            time.sleep(120)  # 2 minutes
    
    # Final summary
    print(f"\n🎉 Batch processing complete!")
    print(f"✅ Successfully processed: {len(successful_dates)} dates")
    print(f"❌ Failed to process: {len(failed_dates)} dates")
    
    if successful_dates:
        print(f"\n📈 Successful dates:")
        for date in successful_dates:
            print(f"  - {date}")
    
    if failed_dates:
        print(f"\n💥 Failed dates:")
        for date in failed_dates:
            print(f"  - {date}")
        print(f"\n💡 You can manually retry failed dates using:")
        print(f"   python scrape_hf_papers.py --date YYYY-MM-DD")

if __name__ == "__main__":
    main()