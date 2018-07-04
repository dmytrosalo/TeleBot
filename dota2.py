import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import tz

BASE_LIQUIPEDIA_URL = 'https://liquipedia.net'


def getTIData():

    try:
        html = urllib.request.urlopen('https://liquipedia.net/dota2/The_International/2018').read()
    except urllib.error.HTTPError:
        print('Error 404 Not Found')
    soup = BeautifulSoup(html, 'html.parser')
    page = soup.find_all('div', class_='mw-parser-output')

    ti_teams=[]
    for item in page:
        ti_teams = item.find_all('div', class_='teamcard')

    team_info_list=[]
    team_info={}
    idx = 0
    for item in ti_teams:
        idx = idx + 1
        name = item.find('center').string
        logo_url = item.div.div.div.img['src']
        # match_time = matches.find('span', attrs={'class':'timer-object timer-object-countdown-only'}).text
        # teams = matches.findAll('span', class_='team-template-text')
        # team_images = matches.findAll('span', class_='team-template-image')
        # print(logo)
        team_info.update({
            'name': name,
            'logo_url': BASE_LIQUIPEDIA_URL + logo_url
            # 'team_2':teams[1].find(text=True),
            # 'team_1_img': BASE_LIQUIPEDIA_URL + team_images[0].find('img')['src'],
            # 'team_2_img':BASE_LIQUIPEDIA_URL + team_images[1].find('img')['src'],
            # 'match_id': idx,
            # 'result': result.strip(),
            # 'match_time': convert_time(match_time)
        })
        team_info_list.append(team_info)
        team_info={}

    return(team_info_list)


def getMatchesData(type):

    try:
        html = urllib.request.urlopen('https://liquipedia.net/dota2/Liquipedia:Upcoming_and_ongoing_matches').read()
    except urllib.error.HTTPError:
        print('Error 404 Not Found')
    soup = BeautifulSoup(html, 'html.parser')
    page = soup.find_all('div', class_='mw-parser-output')

    matches_type=[]
    for item in page:
        matches_type = item.find_all('div', id='infobox_matches')

    ongoing_matches = matches_type[0]
    upcoming_matches = matches_type[1]
    
    text_info=''
    
    if type == 'ongoing':
        text_info = parse_matches(matches_type[0], type)
    elif type == 'upcoming':
        text_info = parse_matches(matches_type[1], type)
    return text_info

def convert_time(time_string):

    date = time_string.replace(' UTC', '')
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    utc = datetime.strptime(date, '%B %d, %Y - %H:%M')
    utc = utc.replace(tzinfo=from_zone)
    central = utc.astimezone(to_zone)
    return central.strftime('%B %d - %H:%M')

def parse_matches(matches_list, type):

    matches_info_list=[]
    matches_info={}
    idx = 0
    for matches in matches_list.findAll('table'):
        idx = idx + 1
        result = matches.find('td', class_='versus').string
        match_time = matches.find('span', attrs={'class':'timer-object timer-object-countdown-only'}).text
        teams = matches.findAll('span', class_='team-template-text')
        team_images = matches.findAll('span', class_='team-template-image')
        # print(team_images)
        matches_info.update({
            'team_1': teams[0].find(text=True),
            'team_2':teams[1].find(text=True),
            'team_1_img': BASE_LIQUIPEDIA_URL + team_images[0].find('img')['src'],
            'team_2_img':BASE_LIQUIPEDIA_URL + team_images[1].find('img')['src'],
            'match_id': idx,
            'result': result.strip(),
            'match_time': convert_time(match_time)
        })
        matches_info_list.append(matches_info)
        matches_info={}
    text_info=''
    for match in matches_info_list:
        text_info =text_info + "Match time: %s\n -> %s  %s  %s \n \n" % (match['match_time'], match['team_1'], match['result'], match['team_2']) 
    return text_info
getTIData()