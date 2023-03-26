import time
from urllib.request import urlopen, Request
import argparse
import logging
from playsound import playsound
from bs4 import BeautifulSoup
from pytz import country_timezones
import os
import time
from urllib.request import urlopen, Request
import argparse
import logging
from playsound import playsound
from bs4 import BeautifulSoup
from pytz import country_timezones
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'
HEADERS = {'User-Agent': USER_AGENT, 'Cookie': 'movies_city=chennai'}
count = 0


def ticketNew():
    global count

    # set this url page that shows all the theater
    url = "https://www.ticketnew.com/Viduthalai-Tickets-Online-Booking-Show-Timings/Release-Date/26556?utm_source=web&utm_medium=scrollbanner&utm_campaign=movie&utm_content=Viduthalai"
    playsound("./BOMB_SIREN-BOMB_SIREN-247265934.mp3")
    req = Request(url, None, HEADERS)
    with urlopen(req) as response:
        html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    required_theaters = ['vettri', 'vidya', 'national']
    q = soup.find_all('div', {"class":
                              "tn-entity-details"})
    theaters = [i.find("h5").text for i in q]
    print(theaters)
    for theater in theaters:
        theaterwords = theater.split(' ')
        for word in theaterwords:
            for req in required_theaters:
                if req == word.lower():
                    while 1:
                        for i in range(10):
                            print(word)
                        playsound("./BOMB_SIREN-BOMB_SIREN-247265934.mp3")
                        pass
    time.sleep(10)
    count += 1
    print(count)
    ticketNew()
    return


def bookMyShow():
    global count
    url = "https://in.bookmyshow.com/buytickets/vikram-chennai/movie-chen-ET00138591-MT/20220604"
    #url = "https://in.bookmyshow.com/buytickets/don-2022-chennai/movie-chen-ET00321832-MT/20220528"
    # url = "https://www.pvrcinemas.com/nowshowing"
    # url = "https://in.bookmyshow.com/explore/home/chennai"
    url = "https://in.bookmyshow.com/buytickets/kannai-nambaathe-chennai/movie-chen-ET00354916-MT/20230325"
    req = Request(url, None, HEADERS)
    while 1:
        # try:
        with urlopen(req) as response:
            html = response.read()
        print(html)
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup.prettify())
        # except :
        #     print(e)
        #     fun()
        #     continue
        # print(soup)
        # <div _ngcontent-c1 = "" class = "title" style = "text-transform:uppercase" > bhool bhulaiyaa 2 < /div >
        q = soup.find_all('div', {"style": "text-transform:uppercase"})
        print(q)
        q = [i.string for i in q]
        print(q)
        if "KC(KrishnaveniCinemas) RG3 LASER DOLBYATMOS TNAGAR" in q or "PVR: Grand Galada, Pallavaram" in q:
            while 1:
                playsound("BOMB_SIREN-BOMB_SIREN-247265934.mp3")
        count += 1
        time.sleep(15)
        print(count)
        # /home/mukesh/Coding/El-Padrino/Workouts/python/bookmyshow-notify/bookmyshow_notify/new.py
    return


# bookMyShow()


ticketNew()
