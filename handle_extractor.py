import requests
from bs4 import BeautifulSoup
import re
import json
import logging

def get_youtube_handle_from_url(url):
    """Extract the handle from a YouTube URL."""
    # Check if the URL is already in the handle format
    handle_match = re.search(r'youtube\.com/(@[\w-]+)', url)
    if handle_match:
        return handle_match.group(1)[1:]  # Return handle without '@'
    
    # If the URL is not in the handle format, fetch the page and scrape the handle
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the script tag containing the JSON data
    for script in soup.find_all("script"):
        if script.string and 'var ytInitialData' in script.string:
            try:
                json_text = script.string.split('var ytInitialData = ')[1].rstrip(' ;')
                json_data = json.loads(json_text)
                tabs = json_data['contents']['twoColumnBrowseResultsRenderer']['tabs']
                for tab in tabs:
                    if 'tabRenderer' in tab:
                        endpoint = tab['tabRenderer']['endpoint']
                        browse_endpoint = endpoint.get('browseEndpoint', {})
                        canonical_base_url = browse_endpoint.get('canonicalBaseUrl', "")
                        if canonical_base_url.startswith("/@"):
                            return canonical_base_url[2:]  # Extract handle without leading '/@'
            except (json.JSONDecodeError, KeyError, IndexError):
                continue
    return None

def extract_handles_from_urls(urls):
    handles = []
    for url in urls:
        handle = get_youtube_handle_from_url(url.strip())
        if handle:
            handles.append(handle)
        else:
            print(f"Handle not found for URL: {url}")
    return ','.join(handles)

# Example list of YouTube channel URLs
channel_urls = "https://www.youtube.com/@handle,https://www.youtube.com/user/username,https://www.youtube.com/c/username,https://www.youtube.com/channel/UC_CHANNEL_ID"

# Split the URLs into a list
channel_urls_list = channel_urls.split(',')

# Get the comma-separated list of handles
handles_list = extract_handles_from_urls(channel_urls_list)
print(handles_list)
