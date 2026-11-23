import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove unnecessary elements
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    text = soup.get_text(" ", strip=True)

    return text


url = "https://example.com"

text = scrape_website(url)

print(text)