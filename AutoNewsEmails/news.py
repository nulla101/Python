# Your API key is: cf30a8a3e3bb4525994f351337f12c3a
import requests


class NewsFeed:
    """Representing multiple news titles and links as a single string.
    """
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "cf30a8a3e3bb4525994f351337f12c3a"

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ''
        number_of_articles = 0
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"
            number_of_articles = number_of_articles + 1
            if number_of_articles == 5:
                break

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = (f"{self.base_url}"
               f"q={self.interest}&"
               f"from={self.from_date}&"
               f"to={self.to_date}&"
               f"language={self.language}&"
               f"apiKey={self.api_key}")
        return url


if __name__ == "__main__":
    news_feed = NewsFeed(interest='cat', from_date='2024-1-16', to_date='2024-1-17', language='en')
    print(news_feed.get())
