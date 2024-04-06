from summariz import *
import requests
from bs4 import BeautifulSoup


def scrape_article(url):
    """
  Scrapes the main content from a given URL.

  Args:
      url (str): The URL of the webpage.

  Returns:
      str: The scraped text content (if successful), empty string otherwise.
  """
    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
            "Upgrade-Insecure-Requests": "1", "DNT": "1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}
        #response = requests.get(url)
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for non-200 status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        # Identify the main content area using appropriate selectors (adjust based on website structure)
        article_body = soup.find("div", class_="article-content")  # Hypothetical class name
        if article_body:
            return article_body.get_text(separator="\n")  # Combine text with newlines
        else:
            return ""  # No content found
    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return ""


def generate_content(urls):
    """
  Generates article content by scraping and summarizing retrieved URLs.

  Args:
      urls (list): A list of URLs to scrape.

  Returns:
      str: The generated article content (combining summaries).
  """
    content = ""
    print(urls)
    scraped_text = scrape_article(urls)
    if scraped_text:
        # Summarize the scraped text (use your preferred summarization technique)
        summary = summarize_text(scraped_text)  # Replace with your summarization function
        content += f"\n**Summary from {urls}:**\n{summary}\n"
        '''
    for url in urls:
        scraped_text = scrape_article(url)
        if scraped_text:
            # Summarize the scraped text (use your preferred summarization technique)
            summary = summarize_text(scraped_text)  # Replace with your summarization function
            content += f"\n**Summary from {url}:**\n{summary}\n"
            
            '''
    print("abc")
    print(content)
    return content


'''
# Example usage (replace with your actual URLs)
urls = ["https://www.example.com/article1", "https://www.example.com/article2"]
content = generate_content(urls)

print(content)
'''
