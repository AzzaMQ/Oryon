#scraper
from newspaper import Article

def get_article(url):

    article = Article(url)

    article.download()

    article.parse()

    title = article.title

    text = article.text

    return title, text