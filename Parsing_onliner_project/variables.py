"""Storage module for class ArticleField"""
from enum import Enum


class ArticleField(Enum):
    """OnlinerHTMLParser application type class"""

    ARTICLE_NAMES = 'article_names'
    ARTICLE_DATE = 'article_date'
    ARTICLE_AUTHOR = 'article_author'
