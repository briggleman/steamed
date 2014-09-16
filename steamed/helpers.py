"""
This script provides a helper function for parsing the additional search
pages from the base search page on store.steampowered.com
"""
import requests
from bs4 import BeautifulSoup

URIS = []

def get_pages(url):
    """
    Grabs the additional page links from the class: 'search_pagination_right' 
    and adds them to the URIS array.
    After the page is added the function is called on itself so that an array
    of all searchable pages is created
    """
    html = requests.get(url)
    
    if html.status_code == 200:
        pagination = BeautifulSoup(html.content).find_all('div', {'class':'search_pagination_right'})
        
        for uri in pagination[0].select('a[href]'):		
            if uri['href'] not in URIS:
                URIS.append(uri['href'])
                get_pages(uri['href'])
                
    return URIS
