#!

import os,sys
from api_footylogic_com.match.statistics.MarketsInfo import getMarketsInfoJson
from api_footylogic_com.match.h2h.RecentformInformation import getRecentformInformationJson
from api_footylogic_com.tournament.Standings import getStandingsJson
from api_footylogic_com.tournament.Competitions import getCompetitionsJson, lookupCompetitionId
from api_footylogic_com.match.h2h.Banner import getBannerJson, getTeams, getCompetitionName
from api_footylogic_com.match.seasonalstats.DropdownFilters import getDropdownFilters

from utils.Statistics import getTopBottomWinningAndLoseing
from utils.WriteExcel import writeExcel
from utils.GetScreenshot import getScreenshot
import nest_asyncio
import asyncio
import ipywidgets as widgets
from bet_hkjc_com.football.getJSON import getMatchesJson, getMatchesList

def genMatchList():
    matches_json = getMatchesJson()
    matches_list = getMatchesList(matches_json)

    labels = []
    for match_label in matches_list.keys():
        labels.append(match_label)

    return [labels, matches_list]