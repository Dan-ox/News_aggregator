from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as Bs


hn = 'https://thehackernews.com/'
tn = 'https://tengrinews.kz/world_news/'
kolesa_news = 'https://kolesa.kz/content/'


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


def get_tn():
    tn_list = []
    r = requests.get(tn).text
    soup = Bs(r, 'lxml')
    posts = soup.find_all('div', {'class': 'tn-article-item'})
    for post in posts:
        rough_title = post.find('span', {'class': 'tn-article-title'})
        rough_path = post.find('a', {'class': 'tn-link'})
        if rough_title is not None and rough_path is not None:
            title = rough_title.text
            url = "https://tengrinews.kz/" + rough_path.get('href')
            data = {'title': title, 'url': url}
            tn_list.append(data)
    return tn_list


def get_kolesa_news():
    kn_list = []
    r = requests.get(kolesa_news).text
    soup = Bs(r, "lxml")
    section = soup.find('section', {'id': 'main-list'})
    posts = section.find_all('li')
    for post in posts:
        title = post.find('h2').text
        url = "https://kolesa.kz/content/" + post.find('a').get('href')
        data = {'title': title, 'url': url}
        kn_list.append(data)
    return kn_list


def home(request):
    context = {'news_list': get_hn(), 'tn_list': get_tn(), 'kn_list': get_kolesa_news()}
    return render(request, 'news/home_page.html', context=context)
