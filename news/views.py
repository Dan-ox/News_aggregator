from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as Bs
import lxml


bbc = 'https://www.bbc.com/news/'
cons = 'https://www.builderonline.com/'
sil = 'https://www.siliconvalley.com/'
hn = 'https://thehackernews.com/'


def get_hn():
    hn_list = []
    r = requests.get(hn).text
    soup = Bs(r, "lxml")
    posts = soup.find_all('div', {'class': 'body-post clear'})
    for post in posts:
        title = post.find('h2', {'class': 'home-title'}).text
        url = post.find('a', {'class': 'story-link'}).get('href')
        data = {'title': title, 'url': url}
        hn_list.append(data)
    return hn_list


def home(request):
    context = {'news': get_hn()}
    return render(request, 'news/home_page.html', context=context)
