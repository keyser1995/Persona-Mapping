"""
Scrapes public-facing profile information from a list of URLs.
Uses requests and BeautifulSoup to extract metadata.
"""
import requests
from bs4 import BeautifulSoup

# Map known domains to patterns or base URLs (expandable)
SUPPORTED_DOMAINS = {
    'github.com': 'https://github.com',
    'twitter.com': 'https://twitter.com',
    # Add more platforms as needed
}


def scrape_profiles(urls):
    """
    For each URL in urls, fetch the page and extract:
      - display name (og:title)
      - bio/description (meta[name=description])
      - profile image URL (og:image)

    Arguments:
    - urls (List[str]): List of profile URLs from Sherlock.

    Returns:
    - List[dict]: List of profile info dicts with keys 'url', 'name', 'bio', 'image'.
    """
    profiles = []

    for url in urls:
        print(f"    [-] Processing: {url}")
        try:
            # HTTP GET request to retrieve the page
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract metadata fields safely
            name_tag = soup.find('meta', {'property': 'og:title'})
            bio_tag = soup.find('meta', {'name': 'description'})
            image_tag = soup.find('meta', {'property': 'og:image'})

            name = name_tag['content'] if name_tag else 'N/A'
            bio = bio_tag['content'] if bio_tag else 'N/A'
            image = image_tag['content'] if image_tag else ''

            # Add to list
            profiles.append({
                'url': url,
                'name': name,
                'bio': bio,
                'image': image
            })

        except requests.RequestException as e:
            print(f"      [!] Request failed: {e}")
        except Exception as e:
            print(f"      [!] Unexpected error: {e}")

    return profiles
