#!/usr/bin/env python3

import os
import sys
import re
import json
import requests
from pprint import pprint


def getMatchesJson():
    url = 'https://bet.hkjc.com/football/getJSON.aspx?jsontype=odds_hil.aspx'

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

    response = requests.get(url, headers=headers)
    response_json = json.loads(response.text)
    # response_json_tournaments = response_json['tournaments']
    response_json_matches = response_json['matches']

    os_cwd = os.getcwd()
    # json_store_path = os_cwd+'/jsons'

    with open("./matches_list.json", 'w+') as f_out_json:
        f_out_json.truncate(0)
        json.dump(response_json_matches, f_out_json)

    # print('get odds_hil done')
    return response_json_matches


def getMatchesList(matches_json):
    output = {}
    for match in matches_json:
        matchDay = match['matchDay']
        matchID = match['matchID']
        matchDate = match['matchDate']
        matchYYYYMMDD = matchDate.split('T')[0]
        tournamentID = match['tournament']['tournamentID']
        tournamentNameEN = match['tournament']['tournamentNameEN']
        tournamentNameCH = match['tournament']['tournamentNameCH']
        homeTeam_teamNameEN = match['homeTeam']['teamNameEN']
        awayTeam_teamNameEN = match['awayTeam']['teamNameEN']
        homeTeam_teamNameCH = match['homeTeam']['teamNameCH']
        awayTeam_teamNameCH = match['awayTeam']['teamNameCH']

        tournament_string = "tournamentNameEN(tournamentNameCH)"
        tournament_string = tournament_string.replace(
            "tournamentNameEN", tournamentNameEN)
        tournament_string = tournament_string.replace(
            "tournamentNameCH", tournamentNameCH)

        vs_string = 'home_en(home_ch) vs away_en(away_ch)'
        vs_string = vs_string.replace('home_en', homeTeam_teamNameEN)
        vs_string = vs_string.replace('away_en', awayTeam_teamNameEN)
        vs_string = vs_string.replace('home_ch', homeTeam_teamNameCH)
        vs_string = vs_string.replace('away_ch', awayTeam_teamNameCH)

        temp = ','.join([matchYYYYMMDD, tournament_string, vs_string])
        output[temp] = [tournamentID, matchID]

    return output
