from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs


bbc = 'https://www.bbc.com/'
cons = 'https://www.builderonline.com/'
sil = 'https://www.siliconvalley.com/'


def get_bbc():
    r = requests.get(bbc)
    soup = bs(r, 'lxml')
    posts = soup.find_all('div', 'class: media-list')
    print(posts)


get_bbc()


def home(request):
    return render(request, 'news/home_page.html')
