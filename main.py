"""
Entry point for My Public Profile Viewer.
Accepts a username or email, runs Sherlock, scrapes public profiles, and generates an HTML report.
"""
import argparse
from sherlock_runner import run_sherlock
from info_scraper import scrape_profiles
from report_generator import generate_report


def main():
    # Set up command-line arguments
    parser = argparse.ArgumentParser(
        description="My Public Profile Viewer: Discover your public footprint"
    )
    # Define mutually exclusive group: either username or email
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--username', help='Username to search across social platforms'
    )
    group.add_argument(
        '--email', help='Email address to check for breach appearances (optional)'
    )
    args = parser.parse_args()

    # Determine identifier (filename-friendly)
    if args.username:
        identifier = args.username
    else:
        # Replace '@' to avoid filesystem issues
        identifier = args.email.replace('@', '_at_')

    # 1. Use Sherlock to find public accounts by username
    if args.username:
        print(f"[+] Running Sherlock for username: {args.username}")
        accounts = run_sherlock(args.username)
    else:
        accounts = []  # No username search when email-only

    # 2. Scrape additional public info from found accounts
    print(f"[+] Scraping public profiles for {len(accounts)} accounts...")
    profiles = scrape_profiles(accounts)

    # 3. Generate an HTML report summarizing the findings
    output_file = f"report_{identifier}.html"
    generate_report(identifier, profiles, output_file)
    print(f"[+] Report generated: {output_file}")


if __name__ == '__main__':
    main()
