#!/usr/bin/env python

from argparse import ArgumentParser as ap
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
import requests


def get_tags(page, html_tag, innertext_only=False):
    if is_url(page):
        page = requests.get(page).text
        soup = bs(page, 'lxml')
    else:
        try:
            with open(page, 'r') as html_file:
                soup = bs(html_file, 'lxml')
        except Exception:
            print(f"'{page}' is not a valid file, exiting...")
            exit(1)

    tags = soup.find_all(html_tag)
    if tags:
        if innertext_only:
            print(f"Fetching inner contents of <{html_tag}> tags...")
            tags = [t.text for t in tags]
        # for line in tags:
        #     print(line)
        return tags
    else:
        print(f'No <{html_tag}> tags found.')
        exit(1)


def is_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except AttributeError:
        return False
