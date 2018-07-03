import urllib.request
from bs4 import BeautifulSoup

def getTitlesFromAll(type):
    # output = ''
    try:
        html = urllib.request.urlopen('https://liquipedia.net/dota2/Liquipedia:Upcoming_and_ongoing_matches').read()
    except urllib.error.HTTPError:
        print('Error 404 Not Found')
    soup = BeautifulSoup(html, 'html.parser')
    page = soup.find_all('div', class_='mw-parser-output')

    matches_type=[]
    for item in page:
        matches_type = item.find_all('div', id='infobox_matches')
        title = item.find('span', id='Ongoing_matches').string
        # h2[title] = title
    ongoing_matches = matches_type[0]
    upcoming_matches = matches_type[1]


    data_list = []
    if type == 'ongoing':
        data_list = ongoing_matches
    elif type == 'upcoming':
        data_list = upcoming_matches
    matches_info_list=[]
    matches_info={}
    idx = 0
    for matches in data_list.findAll('table'):
        idx = idx + 1
        result = matches.find('td', class_='versus').string
        teams = matches.findAll('span', class_='team-template-text')

        matches_info.update({
            'team_1': teams[0].find(text=True),
            'team_2':teams[1].find(text=True),
            'match_id': idx,
            'result': result.strip()
        })
        matches_info_list.append(matches_info)
        matches_info={}

    text_info=''
    for match in matches_info_list:
        text_info =text_info + "%s  %s  %s \n" % (match['team_1'],match['result'],match['team_2']) 

    return text_info
