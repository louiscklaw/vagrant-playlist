#!/usr/bin/env python3

import os
import sys
import requests
import json
from pprint import pprint


# https://api.footylogic.com/match/seasonalstats/dropdown-filters
# ?languageId=19
# &channelId=1
# &tableId=1
# &competitionId=50016467
# &tabId=1

def getDropdownFilters(competitionId="competitionId"):
    url = 'https://api.footylogic.com/match/seasonalstats/dropdown-filters'

    params = {
        'languageId': '19',
        'channelId': '1',
        'tableId': '1',
        'competitionId': competitionId,
        'tabId': '1',
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

    # https://footylogic.com/en/tournament/league/{competitionId}/standings

    with open("./dropdown-filters.json", 'w+') as f_out_json:
        json.dump(response_json_data, f_out_json)

    print('DropdownFilters.py: get getDropdownFilters json done')

    return response_json_data
