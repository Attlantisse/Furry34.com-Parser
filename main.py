import requests
import time
import webbrowser
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup

page = int(input('page number: '))
def furry34_parsing(page):
    try:
        r = requests.get(f'https://furry34.com/page/{page}')
        html = BeautifulSoup(r.content, 'html.parser')
        find_test = html.find('div', class_='box-grid ng-star-inserted').find_all('a')
        print(Fore.GREEN + 'connected to the furry34.com sever')
        for i in find_test:
            links_txt = open('links.txt', 'a')
            links_txt.write('https://furry34.com' + i['href'] + '\n')
            links_txt.close()
        print(Fore.GREEN + 'links was added into the links.txt file')
    except:
        print(Fore.RED + 'something went wrong. please try again')

furry34_parsing(page)