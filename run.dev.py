#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Shows how to control GoogleScraper programmatically.
"""

import sys
from GoogleScraper import scrape_with_config, GoogleSearchError
from GoogleScraper.database import ScraperSearch, SERP, Link


def related_search():
    target_directory = 'related/'

    # See in the config.cfg file for possible values
    config = {
            'keyword': 'web siling', # :D hehe have fun my dear friends
            'search_engines': 'yahoo', # duckduckgo not supported
            'search_type': 'related',
            'scrapemethod': 'selenium'
    }

    try:
        sqlalchemy_session = scrape_with_config(config)
    except GoogleSearchError as e:
        print(">>>", e)

    for search in sqlalchemy_session.query(ScraperSearch).all():
        for serp in search.serps:
            # print(serp, dir(serp))
            for keyword in serp.keywords:
                print(keyword)

### MAIN FUNCTION ###

if __name__ == '__main__':
    related_search()
