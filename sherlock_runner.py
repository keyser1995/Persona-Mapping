"""
Module to run Sherlock and parse results programmatically.
"""
import subprocess
import json
import tempfile
import os


def run_sherlock(username):
    """
    Executes the Sherlock CLI for a given username.
    Returns a list of profile URLs where the username was found.

    Arguments:
    - username (str): The username to search for.

    Returns:
    - List[str]: URLs of found profiles.
    """
    # Create a temporary directory to hold JSON output
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, 'results.json')
        # Call Sherlock as a subprocess with JSON output
        subprocess.run([
            'sherlock',               # sherlock executable
            username,                 # search term
            '--output', output_path,  # where to save JSON
            '--json'                  # request JSON format
        ], check=True)

        # Read the JSON results
        with open(output_path, 'r') as f:
            data = json.load(f)

    # Filter: only include profiles where status == 'found'
    found_profiles = []
    for entry in data:
        if entry.get('status') == 'found':
            found_profiles.append(entry.get('profile'))

    return found_profiles
