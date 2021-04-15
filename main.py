from bs4 import BeautifulSoup
import requests
import smtplib
html_doc = requests.get("https://news.ycombinator.com/").text
soup = BeautifulSoup(html_doc, 'html.parser')


articles = soup.find_all("a", class_="storylink")
article_texts = [article_tag.getText() for article_tag in articles]
article_links = [article_tag.get("href") for article_tag in articles]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_upvotes = article_upvotes.index(max(article_upvotes))
print(article_texts[max_upvotes])
print(article_links[max_upvotes])
print(max(article_upvotes))
