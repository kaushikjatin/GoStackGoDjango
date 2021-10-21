from django.http.request import host_validation_re
from django.http.response import Http404
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


def profit_calculator(ap, fb, ggl, ama):
    profit = ap*(apple["m2"]-apple["m1"]) + fb*(facebook["m2"] - facebook["m1"]) + \
        ggl*(google["m2"] - google["m1"]) + ama*(amazon["m2"]-amazon["m1"])
    cost = ap*(apple["m1"]) + fb*(facebook["m1"]) + \
        ggl*(google["m1"]) + ama*(amazon["m1"])
    return (profit*100/cost)


def homepage(request):
    return render(request, "news.html")


def stock_game(request):
    return render(request, "stock_game.html")


def calculation(request):

    share_apple = int(request.POST.get('apple'))
    share_facebook = int(request.POST.get('facebook'))
    share_amazon = int(request.POST.get('amazon'))
    share_google = int(request.POST.get('google'))
    # rem_cash = int(request.POST.get('leftover'))
    total_share = share_amazon + share_facebook + \
        share_apple + share_google
    if (total_share > 100):
        return render(request, "page404.html", {"error": "More than 100 percent reduce it"})
    elif (total_share < 100):
        return render(request, "page404.html", {"error": "Less than 100 percent increase it"})

    p_profit = profit_calculator(share_apple, share_facebook,
                                 share_google, share_amazon)
    avg_profit = profit_calculator(25, 25, 25, 25)

    return render(request, "page404.html", {"success": True, "p_profit": p_profit, "avg_profit": avg_profit})


def news(request):
    query = request.POST.get("news", False)

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
    descriptions = []
    res = descriptions
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
    data = []
    for i in range(0, len(clean_links)):
        new_data = titles[i] + descriptions[i] + clean_links[i]
        data.append(new_data)
        print(titles[i])
        print(descriptions[i])
        print(clean_links[i])
        print()

    return render(request, "news.html", {"titles": titles, "data": data, "descriptions":  descriptions, "links": clean_links})


def stock_prediction(request):
    return HttpResponse("This is stock prediction page")
