from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest
import urllib
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re

google = {"m1": 1341.550049, "m2": 1462}
facebook = {"m1": 206.75, "m2": 203.440002}
amazon = {"m1": 1875, "m2": 2010.599976}
apple = {"m1": 74.059998, "m2": 76.074997}


def homepage(request):
    return render(request, "news.html")


def stock_game(request):
    return render(request, "stock_game.html")


def news(request):
    res = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    query = "google"

    query = urllib.parse.quote_plus(query)  # Format into URL encoding
    number_result = 50
    ua = UserAgent()

    google_url = "https://www.google.com/search?q=" + \
        query + "&num=" + str(number_result)
    response = requests.get(google_url, {"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "html.parser")

    result_div = soup.find_all('div', attrs={'class': 'ZINbbc'})

    links = []
    titles = []
    res = titles
    descriptions = []
    for r in result_div:
        # Checks if each element is present, else, raise exception
        try:
            link = r.find('a', href=True)
            title = r.find('div', attrs={'class': 'vvjwJb'}).get_text()
            description = r.find('div', attrs={'class': 's3v9rd'}).get_text()

            # Check to make sure everything is present before appending
            if link != '' and title != '' and description != '':
                links.append(link['href'])
                titles.append(title)
                descriptions.append(description)
        # Next loop if one element is not present
        except:
            continue

    to_remove = []
    clean_links = []
    for i, l in enumerate(links):
        clean = re.search('\/url\?q\=(.*)\&sa', l)

        # Anything that doesn't fit the above pattern will be removed
        if clean is None:
            to_remove.append(i)
            continue
        clean_links.append(clean.group(1))

    # Remove the corresponding titles & descriptions
    for x in to_remove:
        del titles[x]
        del descriptions[x]

    for i in range(0, len(clean_links)):
        print(titles[i])
        print(descriptions[i])
        print(clean_links[i])
        print()
    return render(request, "news.html", {"result": res})
