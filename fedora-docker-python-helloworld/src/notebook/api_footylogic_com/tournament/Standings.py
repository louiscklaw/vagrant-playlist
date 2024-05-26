#!/usr/bin/env python
import os
import sys
import requests
import json
from pprint import pprint

USE_TEST_URL = int(os.getenv('USE_TEST_URL', False))

# https://api.footylogic.com/tournament/standings?
# languageId=19
# &channelId=1
# &competitionId=50016467
# &optionId=1
# &seasonId=4418
# &layoutId=1
# &roundId=13410
# &tabId=1
# &group=all


def getStandingsJson(competition_id, season_id, round_id):

    url = 'https://api.footylogic.com/tournament/standings'
    test_url = 'http://localhost:8081/tournament/standings/standings.json'
    url = [url, test_url][USE_TEST_URL]

    params = {
        'languageId': '19',
        'channelId': '1',
        'competitionId': str(competition_id),
        'optionId': '1',
        'seasonId': str(season_id),
        'layoutId': '1',
        'roundId': str(round_id),
        'tabId': '1',
        'group': 'all',
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

    with open(json_store_path+"/standings.json", 'w+') as f_out_json:
        f_out_json.truncate(0)
        json.dump(response_json_data, f_out_json)

    print('Standings.py: get standings done')
    return response_json_data
