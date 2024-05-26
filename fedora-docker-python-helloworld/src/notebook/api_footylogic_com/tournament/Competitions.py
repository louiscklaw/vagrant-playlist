#!/usr/bin/env python
import os
import sys
import requests
import json


def getCompetitionsJson():
    url = 'https://api.footylogic.com/tournament/competitions'

    params = {
        'languageId': '19',
        'channelId': '1',
        'categoryId': '1'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://footylogic.com/',
        'Origin': 'https://footylogic.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }

    response = requests.get(url, params=params, headers=headers)
    response_json = json.loads(response.text)

    # from pprint import pprint
    # https://footylogic.com/en/tournament/league/{competitionId}/standings

    expanded_json = response_json
    for data in expanded_json['data']:
        for competition in data['competitions']:
            competitionId = str(competition['competitionId'])
            competition['standing_table_link'] = 'https://footylogic.com/en/tournament/league/' + \
                competitionId+'/standings'

    with open("./competitions.json", 'w+') as f_out_json:
        f_out_json.truncate(0)
        json.dump(expanded_json['data'], f_out_json)

    return expanded_json['data']


def lookupCompetitionId(competitions_json, competitionName):
    for category in competitions_json:
        for competition in category['competitions']:
            if competition['competitionName'] == competitionName:
                return competition['competitionId']

    return 'not found'
