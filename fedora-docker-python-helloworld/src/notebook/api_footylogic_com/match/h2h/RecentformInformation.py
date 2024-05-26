#!/usr/bin/env python
import os
import sys
import requests
import json


# https://api.footylogic.com/match/h2h/recentform-information
# ?languageId=19
# &channelId=1
# &homeTeamId=50003297
# &awayTeamId=50000948
# &marketGroupId=1
# &optionIdH=1
# &optionIdA=1
# &mode=1

def getRecentformInformationJson(homeTeamId, awayTeamId):

    # https://api.footylogic.com/match/h2h/recentform-information?languageId=19&channelId=1&homeTeamId=50000180&awayTeamId=50000599&marketGroupId=1&optionIdH=1&optionIdA=1&mode=1
    url = 'https://api.footylogic.com/match/h2h/recentform-information'

    params = {
        'languageId': '19',
        'channelId': '1',
        'homeTeamId': homeTeamId,
        'awayTeamId': awayTeamId,
        'marketGroupId': '1',
        'optionIdH': '1',
        'optionIdA': '1',
        'mode': '1'
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

    # https://footylogic.com/en/tournament/league/{competitionId}/standings

    os_cwd = os.getcwd()
    json_store_path = os_cwd+'/jsons'

    with open(json_store_path+"/recentfrom-information.json", 'w+') as f_out_json:
        json.dump(response_json['data'], f_out_json)

    return response_json['data']
