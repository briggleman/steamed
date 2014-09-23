"""
Steamed is a spider for scraping sales data from Steam

usage:
>>> import steamed
>>> sales = steamed.sales()
>>> sales
[{'game': u'Substance Indie Pack', 'full': u'249.99', 'sale': u'199.99', 'img': 'http://cdn.akamai.steamstatic.com/steam/apps/287280/capsule_sm_120.jpg?t=1395117312', 'appid': '287280'}]
"""

__title__ = 'steamed'
__version__ = '1.2.2'
__author__ = 'Ben Riggleman'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2014 Ben Riggleman'

import requests
import re
from bs4 import BeautifulSoup
from . import helpers

RGXIMG = re.compile("(?<=apps\/)([0-9]{3,6})|(?<=subs\/)([0-9]{3,6})")
SEARCH_URL = 'http://store.steampowered.com/search/?sort_by=&sort_order=ASC&specials=1&page=1'

def sales():
    """
    Grabs all the games on sale in the Steam store at store.steampowered.com
    No url is required, defaults to the specials starting on page 1
    The helper function get_pages(url) scrapes the additional pagination links
    from each page and adds it to an array so that they are not processed 
    mutiple times 
    """
    items = []
    uris = helpers.get_pages(SEARCH_URL)
    
    for uri in uris:
        html = requests.get(uri)

        if html.status_code == 200:
            games = BeautifulSoup(html.content.decode('UTF-8')).find_all('a', {'class':'search_result_row'})

            for game in games:
                try:
                    values = {}
                    platforms = []
                    prices = game.find('div', {'class':'search_price'}).text.strip()
                    img = game.find('img', {'width':'120'})['src']
                    values['game'] = game.find('span', {'class':'title'}).text
                    values['img'] = str(img)
                    values['appid'] = re.search(RGXIMG, str(img)).group()
                    blank, values['full'], values['sale'] = prices.split('$')
                    values['pct'] = game.find('div', {'class':'search_discount'}).text.strip()
                    values['released'] = game.find('div', {'class':'search_released'}).text
                    
                    if not game.find('span', {'class':'search_review_summary'}) is None:
                        values['review'], values['summary'] = game.find('span', {'class':'search_review_summary'})['data-store-tooltip'].split('<br>')
                    else:
                        values['review'] = ''
                        values['summary'] = ''

                    if not game.find('span', {'class':'platform_img win'}) is None: platforms.append('win')
                    if not game.find('span', {'class':'platform_img mac'}) is None: platforms.append('mac')
                    if not game.find('span', {'class':'platform_img steamplay'}) is None: platforms.append('steamplay')
                    if not game.find('span', {'class':'platform_img linux'}) is None: platforms.append('linux')

                    values['platforms'] = platforms

                    items.append(values)
                except:
                    pass
    return items
