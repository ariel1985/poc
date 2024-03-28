import requests

def download_content_url(url):
    print(f"Downloading {url}")
    
    # Get the HTML content from url
    response = requests.get(url)
    html = response.text
    
    # Save the HTML content to a file
    with open("data/chat4u.html", "w") as f:
        f.write(html)
        
    print(f"Downloaded {url}")


if __name__ == "__main__":
    
    URL = "https://chat4u.store"
    download_content_url(URL)