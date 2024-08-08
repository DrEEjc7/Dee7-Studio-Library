import requests
import json
import os

def get_webflow_pages(site_id, api_key):
    url = f"https://api.webflow.com/sites/{site_id}/pages"
    headers = {
        "accept-version": "1.0.0",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def main():
    site_id = "663df7a0abb81427d879d9e0"
    api_key = os.environ.get("WEBFLOW_API_KEY")
    
    if not api_key:
        raise ValueError("WEBFLOW_API_KEY environment variable is not set")

    pages = get_webflow_pages(site_id, api_key)
    
    sitemap = [{"title": page["name"], "url": f"https://ui-library-dee7studio.webflow.io{page['slug']}"} for page in pages]
    
    with open('sitemap.json', 'w') as f:
        json.dump(sitemap, f, indent=2)

    print(f"Generated sitemap.json with {len(sitemap)} pages.")
    print("Sitemap content preview:")
    print(json.dumps(sitemap[:5], indent=2))  # Print first 5 entries for verification

if __name__ == "__main__":
    main()