#!/usr/bin/env python3

import os,sys,json
from pprint import pprint

def distillRecent8Results(json_manifest, competitionName="Belgian Division 1"):
    # distill results
    json_manifest['statistics']['distilledRecent8Results'] = {}
    json_manifest_distilled = json_manifest['statistics']['distilledRecent8Results']
    json_manifest_distilled['homeTeam'] = []
    distilled_homeTeam = json_manifest_distilled['homeTeam']
    json_manifest_distilled['awayTeam'] = []
    distilled_awayTeam = json_manifest_distilled['awayTeam']

    recent8Results = json_manifest['recentfrom-information.json']['recent8Results']
    recent8ResultsHomeTeam = json_manifest['recentfrom-information-home-team.json']['recent8Results']
    recent8ResultsAwayTeam = json_manifest['recentfrom-information-away-team.json']['recent8Results']

    homeTeam = recent8ResultsHomeTeam['homeTeam']
    for result in homeTeam:
        if result['competitionName'] == competitionName and result['homeOrAway'] == "H":
            if (len(distilled_homeTeam)) < 5:
              distilled_homeTeam.append(result)

    awayTeam = recent8ResultsAwayTeam['awayTeam']
    for result in awayTeam:
        if result['competitionName'] == competitionName and result['homeOrAway'] == "A":
            if (len(distilled_awayTeam)) < 5:
              distilled_awayTeam.append(result)

def lookupPositionByTeamName(json_manifest, teamNameToCheck):
    standings_info = json_manifest['tournament/standings.json']['info']
    for standing in standings_info:
        if standing['teamName'] == teamNameToCheck:
            return standing['teamRank']

    raise Exception(teamNameToCheck)
    return -99

def countTotalStandingTeam(json_manifest):
    standings_info = json_manifest['tournament/standings.json']['info']

    return len(standings_info)

def getTopBottomWinningAndLoseing(json_manifest, competitionName):
    json_manifest['statistics'] = {}
    json_manifest['statistics']['top_bottom_winning_losing'] = {}
    result = json_manifest['statistics']['top_bottom_winning_losing']

    # get statistics
    result['home_top_win_count'] = 0
    result['home_top_draw_count'] = 0
    result['home_top_loss_count'] = 0
    result['home_bottom_win_count'] = 0
    result['home_bottom_draw_count'] = 0
    result['home_bottom_loss_count'] = 0

    result['away_top_win_count'] = 0
    result['away_top_draw_count'] = 0
    result['away_top_loss_count'] = 0
    result['away_bottom_win_count'] = 0
    result['away_bottom_draw_count'] = 0
    result['away_bottom_loss_count'] = 0

    # filter all non same tournament
    distillRecent8Results(json_manifest, competitionName)

    json_manifest_distilled = json_manifest['statistics']['distilledRecent8Results']
    json_manifest_distilled_homeTeam = json_manifest_distilled['homeTeam']
    json_manifest_distilled_awayTeam = json_manifest_distilled['awayTeam']

    all_team_count = countTotalStandingTeam(json_manifest)
    json_manifest_distilled['allTeamCount'] = all_team_count

    for entry in json_manifest_distilled_homeTeam:
        oppTeamName = entry['oppTeamName']
        pos = lookupPositionByTeamName(json_manifest, oppTeamName)
        pos = int(pos)
        entry['pos'] = pos

        if (pos <= (all_team_count / 2)):
            # count home top winning
            if entry['fullTimeResult'] == 'W':
                result['home_top_win_count'] += 1
            # count home top draw
            if entry['fullTimeResult'] == 'D':
                result['home_top_draw_count'] += 1
            # count home top losing
            if entry['fullTimeResult'] == 'L':
                result['home_top_loss_count'] += 1
        else:
            # count home bottom winning
            if entry['fullTimeResult'] == 'W':
                result['home_bottom_win_count'] += 1
            # count home bottom draw
            if entry['fullTimeResult'] == 'D':
                result['home_bottom_draw_count'] += 1
            # count home bottom losing
            if entry['fullTimeResult'] == 'L':
                result['home_bottom_loss_count'] += 1

    for entry in json_manifest_distilled_awayTeam:
        oppTeamName = entry['oppTeamName']
        pos = lookupPositionByTeamName(json_manifest, oppTeamName)
        pos = int(pos)
        entry['pos'] = pos

        if (pos <= (all_team_count / 2)):
            # count away top winning
            if entry['fullTimeResult'] == 'W':
                result['away_top_win_count'] += 1

            # count away top draw
            if entry['fullTimeResult'] == 'D':
                result['away_top_draw_count'] += 1

            # count away top losing
            if entry['fullTimeResult'] == 'L':
                result['away_top_loss_count'] += 1
        else:
            # count away bottom winning
            if entry['fullTimeResult'] == 'W':
                result['away_bottom_win_count'] += 1
            # count away bottom draw
            if entry['fullTimeResult'] == 'D':
                result['away_bottom_draw_count'] += 1
            # count away bottom losing
            if entry['fullTimeResult'] == 'L':
                result['away_bottom_loss_count'] += 1

def helloworld():
    print("helloworld")
