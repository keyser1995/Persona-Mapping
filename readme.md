# My Public Profile Viewer

**Overview**
A tool to help users check what information about them (username or email) is publicly accessible online. Integrates with [Sherlock](https://github.com/sherlock-project/sherlock) and scrapes public profile data.

## Features
- **Username search** via Sherlock
- **Email breach check** via HaveIBeenPwned API (optional)
- **Public profile scraping** for display name, bio, profile picture, and location clues
- **Report generation**: HTML report summarizing findings with images and alerts

## Prerequisites
- Python 3.8+
- Git

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/my-public-profile-viewer.git
cd my-public-profile-viewer

# Create and activate a virtual environment
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
