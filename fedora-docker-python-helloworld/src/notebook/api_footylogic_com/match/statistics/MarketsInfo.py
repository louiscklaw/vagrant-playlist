#!/usr/bin/env python
import os
import sys
import requests
import json


def getMarketsInfoJson(eventId, homeTeamId, awayTeamId, competitionId):
    # https://api.footylogic.com/match/statistics/markets-info?channelId=1&languageId=1&eventId=50024534&seasonId=1&homeTeamId=50000180&awayTeamId=50000599&competitionId=50024169
    url = 'https://api.footylogic.com/match/statistics/markets-info'

    params = {
        'languageId': '19',
        'channelId': '1',
        'eventId': eventId,
        'seasonId': '1',
        'homeTeamId': homeTeamId,
        'awayTeamId': awayTeamId,
        'competitionId': competitionId,
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
    response_json_data = response_json['data']

    os_cwd = os.getcwd()
    json_store_path = os_cwd+'/jsons'

    with open(json_store_path+"/markets-info.json", 'w+') as f_out_json:
        f_out_json.truncate(0)
        json.dump(response_json_data, f_out_json)

    # https://footylogic.com/en/tournament/league/{competitionId}/standings

    print('MarketsInfo.py: getMarketsInfoJson done')

    return response_json_data
