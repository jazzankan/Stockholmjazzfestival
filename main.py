import requests
from bs4 import BeautifulSoup
import json

from feedAPI import feed_it

response = requests.get("https://stockholmjazz.se/")
festival_page = response.text

soup = BeautifulSoup(festival_page, "html.parser")
#Gör en lista med konserter
specific_class = 'thumb--program'
event_list = soup.find_all('li',class_=specific_class)
#lista att ladda upp till valuefile
add_to_jsonlist = []

with open('valuefile.json', 'r') as f:
    old_values_list = json.load(f)
    for event in event_list:
        event = str(event)
        item_soup = BeautifulSoup(event, "html.parser")
        # Hitta 'li'
        li_tag = item_soup.find('li')
        # Värdet av li-attributet 'data-artst'
        artst_value = li_tag['data-artst']
        if int(artst_value) not in old_values_list:
            artist = item_soup.h2.getText()
            artist = artist.strip()
            date = li_tag['data-date']
            time = li_tag['data-time']
            link_tags = item_soup.find_all('a')
            link = link_tags[0]['href']
            stage_comment = link_tags[2].getText()
            add_to_jsonlist.append(int(artst_value))
            print(artist)
            print(date)
            print(time)
            print(link)
            print(stage_comment)
            print('----------')
            if add_to_jsonlist:
                user_input = input("Mata in posten? j/n:\n")
                if user_input == "j":
                    feed_it(artist,date,time,link, stage_comment)

with open('valuefile.json', 'w') as f:
    if add_to_jsonlist:
        jsonlist = old_values_list + add_to_jsonlist
        json.dump(jsonlist,f)
        print("Sparat till Valuefile")
    else:
        json.dump(old_values_list, f)
        print("Inga nya konserter!")
