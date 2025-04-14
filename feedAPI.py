import requests

def feed_it(artist,date,time,link, stage_comment):
    # Utvecklingsurl. OBS place_id och organizer_id måste ändras beroende på miljö:
    # place_id för utvecklingsmiljön : 1
    #org_id för utvecklingsmiljön: 5
    #place_ id för skarpa: 1
    #org_id för skrapa: 83
    #url = 'http://localhost/api/v1/events'
    #Nyckel utvecklingsmiljön: 2|MDybuSA2L23uICjpYchwoqF07enRpwvuuiYD11Y32f517b7a
    #Nyckel skarpa: 2|CYXAKvuNNEnSlAiy2BgvkPaimuIwXGVMZDMT37M69b25751f
    #url = 'http://localhost/api/v1/events'
    url = 'https://jazztider.webbsallad.se/api/v1/events'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization':  "Bearer " + 'MY_KEY', 'accept': 'application/json'}
    data = {'name': artist, 'place_id': '1', 'organizer_id': '83', 'day': date,'timeofday': time, 'link': link, 'comment': 'Scen: ' + stage_comment}
    post_req = requests.post(url,headers=headers, data=data)
    if post_req.status_code != 200:
        print("APIET HAR INTE TAGIT EMOT POSTEN!")
