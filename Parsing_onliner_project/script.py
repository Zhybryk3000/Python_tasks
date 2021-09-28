from categories import MainOnlinerPageLinks
from categories import OnlinerCategory
from categories import OnlinerArticle

if __name__ == '__main__':
    d = OnlinerCategory('https://money.onliner.by/')
    print(d.onliner_articles)

    s = MainOnlinerPageLinks('https://www.onliner.by/')
    print(s.onliner_links)

    r = OnlinerArticle('https://auto.onliner.by/2021/09/27/v-velikobritanii-deficit-topliva')
    print(r.onliner_articles)
