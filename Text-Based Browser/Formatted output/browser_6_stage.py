from sys import argv
from os import mkdir
from os import path
from _collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore

if not (len(argv) == 2 and argv[1]):
    exit()


def parse_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    nodes = list(soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a']))
    text = "\n".join([(Fore.BLUE if node.name == 'a' else '') + node.getText()
                      for node in nodes])
    print(text)
    return text


def load_page(page, new=False):
    global tabs
    parts = page.split(".")
    site_name = ".".join(parts[:-1]) if len(parts) > 1 else page

    if new:
        tabs.add(site_name)
        with open(f"tb_tabs/{site_name}.txt", "w") as file:
            url = ("https://" if "https://" not in page else "") + page
            try:
                r = requests.get(url)
                if r:
                    file.write(parse_content(r.content))
            except requests.ConnectionError as _exception:
                print("Error: Incorrect URL")
    else:
        with open(f"tb_tabs/{site_name}.txt", "r") as file:
            parse_content(file.read())


if not path.exists(argv[1]):
    mkdir(argv[1])
tabs = set()
pages = deque()

current_page = ''
while True:
    if current_page == 'back':
        if pages:
            pages.pop()
            current_page = pages.pop()
        else:
            current_page = ''
            continue
    else:
        current_page = input()

    if current_page in tabs:
        pages.append(current_page)
        load_page(current_page)
    elif current_page == 'back':
        continue
    elif current_page == 'exit':
        break
    else:
        pages.append(current_page)
        load_page(current_page, True)
