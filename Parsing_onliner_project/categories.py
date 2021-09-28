"""Storage module for class OnlinerArticle, OnlinerCategory and MainOnlinerPageLinks"""
from typing import List

from parsing import OnlinerHTMLParser
from httpRequests import HTTPClient


class OnlinerArticle:
    """Class for gets information about articles"""
    DEFAULT_HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                     ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

    def __init__(self, url_article):
        """
        :param url_article: article url address
        """
        self.url = url_article
        self.onliner_articles = self.__get_articles_info()

    def __get_articles_info(self) -> List[dict]:
        """
        Method for gets information from articles
        :return: list with information about article name, article date and article author for articles
        """
        response = HTTPClient.get(self.url, OnlinerArticle.DEFAULT_HEADERS)
        if response.status_code == 200:
            articles_info = OnlinerHTMLParser.parser_onliner_articles(response.text)
            return articles_info
        print(f'Error with {OnlinerArticle.__get_articles_info.__name__}')


class OnlinerCategory:
    """Class for gets articles links"""

    def __init__(self, url_category):
        """
        :param url_category: categories url address
        """
        self.url = url_category
        self.onliner_articles = self.__get_articles_links()

    def __get_articles_links(self) -> List[OnlinerArticle]:
        """
        Method for gets all categories links
        :return: list with object class OnlinerArticle
        """
        response = HTTPClient.get(self.url, OnlinerArticle.DEFAULT_HEADERS)
        if response.status_code == 200:
            articles_links = OnlinerHTMLParser.parser_onliner_articles_link(response.text)
            return [OnlinerArticle(link) for link in articles_links]
        print(f'Error with {OnlinerCategory.__get_articles_links.__name__}')


class MainOnlinerPageLinks:
    """Class for gets categories links"""

    def __init__(self, url, exception=None):
        """
        :param url: main page url code
        :param exception: used for exclusion something from result
        """
        self.url = url
        self.exception = exception
        self.onliner_links = self.__get_onliner_categories_links()

    def __get_onliner_categories_links(self) -> List[OnlinerCategory]:
        """
        Method for gets all categories links
        :return: list with object class OnlinerCategory
        """
        response = HTTPClient.get(self.url, OnlinerArticle.DEFAULT_HEADERS)
        if response.status_code == 200:
            categories_links = OnlinerHTMLParser.parser_onliner_categories_link(response.text, self.exception)
            return [OnlinerCategory(link) for link in categories_links]
        print(f'Error with {MainOnlinerPageLinks.__get_onliner_categories_links.__name__}')
