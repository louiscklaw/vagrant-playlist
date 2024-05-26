#!/usr/bin/env python3

import os
import sys
import json
from pprint import pprint

from api_footylogic_com.match.statistics.MarketsInfo import getMarketsInfoJson
from api_footylogic_com.match.h2h.RecentformInformation import getRecentformInformationJson
from api_footylogic_com.match.h2h.RecentformInformationHomeTeam import getRecentformInformationHomeTeamJson
from api_footylogic_com.match.h2h.RecentformInformationAwayTeam import getRecentformInformationAwayTeamJson
from api_footylogic_com.tournament.Standings import getStandingsJson
from api_footylogic_com.tournament.Competitions import getCompetitionsJson, lookupCompetitionId
from api_footylogic_com.tournament.Options import getOptionsJson
from api_footylogic_com.match.h2h.Banner import getBannerJson, getTeams, getCompetitionName
from api_footylogic_com.match.seasonalstats.DropdownFilters import getDropdownFilters

from utils.Statistics import getTopBottomWinningAndLoseing
from utils.WriteExcel import writeExcel
from utils.GetScreenshot import getScreenshot, getScreenshot_bmstatistics, getScreenshot_bmrecentforms, getScreenshot_standings
import nest_asyncio
import asyncio


def genExcelReport(tournamentID='50022259', matchID='50024766', report_filename="report.xlsx"):
    competitionId = tournamentID
    eventId = matchID

    # # extract
    # # # banner.py
    banner_json = getBannerJson(eventId)
    [homeTeamId, awayTeamId] = getTeams(banner_json)
    competitionName = getCompetitionName(banner_json)

    # # # # 'https://footylogic.com/en/matchcenter/0/'+tournamentID+'/'+matchID+'/bmrecentforms'

    # # match/h2h/RecentformInformation.py
    getRecentformInformationJson(homeTeamId, awayTeamId)
    getRecentformInformationHomeTeamJson(homeTeamId, awayTeamId)
    getRecentformInformationAwayTeamJson(homeTeamId, awayTeamId)

    # # MarketsInfo.py
    getMarketsInfoJson(eventId, homeTeamId, awayTeamId, competitionId)

    competitions_json = getCompetitionsJson()
    # competitionId = lookupCompetitionId(competitions_json, competitionName)
    lookupCompetitionId(competitions_json, competitionName)

    dropdown_filters_json = getDropdownFilters(competitionId)
    seasonId = dropdown_filters_json['Season'][0]['id']

    options_json = getOptionsJson(competitionId, seasonId)
    roundId = options_json[0]['id']


    # https://api.footylogic.com/tournament/options?languageId=19&channelId=1&competitionId=50019599&seasonId=4456
    standings_json = getStandingsJson(competitionId, seasonId, roundId)

    # translate
    json_manifest = {}
    pattern = r"(?<={jp:)(.*)(?=})"

    os_cwd = os.getcwd()
    utils_path = os_cwd+'/utils'
    excel_template_path = '/report_template.xlsx'

    json_store_path = os_cwd+'/jsons'
    output_path = os_cwd + "/_output"
    images_path = os_cwd + "/_images"

    markets_info_json_path = json_store_path+'/markets-info.json'
    recentform_information_json_path = json_store_path+'/recentfrom-information.json'
    recentform_information_home_team_json_path = json_store_path+'/recentfrom-information-home-team.json'
    recentform_information_away_team_json_path = json_store_path+'/recentfrom-information-away-team.json'
    recentform_information_json_path = json_store_path+'/recentfrom-information.json'
    standings_json_path = json_store_path+'/standings.json'
    banner_json_path = json_store_path+'/banner.json'
    json_manifest_json_path = json_store_path+'/json_manifest.json'

    with open(banner_json_path, 'r') as json_file:
        banner_json = json.load(json_file)
        json_manifest = {**json_manifest, 'banner_json': banner_json}

    with open(markets_info_json_path, 'r') as json_file:
        markets_info_json = json.load(json_file)
        json_manifest = {**json_manifest,
                         'markets-info.json': markets_info_json}

        # to be obsoleted
        json_manifest = {**json_manifest, **markets_info_json}

    with open(recentform_information_json_path, 'r') as json_file:
        recentfrom_information_json = json.load(json_file)
        json_manifest = {
            **json_manifest, 'recentfrom-information.json': recentfrom_information_json}

        # to be obsoleted
        json_manifest = {**json_manifest, **recentfrom_information_json}

    with open(recentform_information_home_team_json_path, 'r') as json_file:
        recentfrom_information_json = json.load(json_file)
        json_manifest = {
            **json_manifest, 'recentfrom-information-home-team.json': recentfrom_information_json}

        # to be obsoleted
        json_manifest = {**json_manifest, **recentfrom_information_json}

    with open(recentform_information_away_team_json_path, 'r') as json_file:
        recentfrom_information_json = json.load(json_file)
        json_manifest = {
            **json_manifest, 'recentfrom-information-away-team.json': recentfrom_information_json}

        # to be obsoleted
        json_manifest = {**json_manifest, **recentfrom_information_json}

    with open(standings_json_path, 'r') as json_file:
        standings_json = json.load(json_file)
        json_manifest = {**json_manifest,
                         'tournament/standings.json': standings_json}

    with open(json_manifest_json_path, 'w+') as f_out:
        f_out.truncate(0)
        json.dump(json_manifest, f_out)

    # get top/bottom winning and loseingreport_filename
    getTopBottomWinningAndLoseing(json_manifest, competitionName)

    # get screenshot
    nest_asyncio.apply()
    bms_url = 'https://footylogic.com/en/matchcenter/0/' + tournamentID+'/'+ matchID +'/bmstatistics'
    bm_recent = 'https://footylogic.com/en/matchcenter/0/' + tournamentID+'/'+ matchID +'/bmrecentforms'
    standings_url = 'https://footylogic.com/en/tournament/league/' + tournamentID +'/standings'

    print(bms_url)
    print(bm_recent)
    print(standings_url)
    asyncio.run(getScreenshot_bmstatistics(bms_url, images_path+'/bmstatistics.png', 1))
    asyncio.run(getScreenshot_bmrecentforms(bm_recent, images_path+'/bmrecentforms.png', 1))
    asyncio.run(getScreenshot_standings(standings_url, images_path+'/standings.png', 1))

    # load
    writeExcel(json_manifest, [
        images_path+'/bmstatistics.png',
        images_path+'/bmrecentforms.png',
        images_path+'/standings.png',
    ], report_filename)

    print('reports.py: done...')


def helloworld():

    print("helloworld")
