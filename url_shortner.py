import requests

def shorten_url(url):
    try:
        response = requests.get(f"http://tinyurl.com/api-create.php?url={url}")
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException:
        return None

# Example usage
original_url = "http://saimulhoque.me/"
short_url = shorten_url(original_url)
print("Shortened URL:", short_url)
