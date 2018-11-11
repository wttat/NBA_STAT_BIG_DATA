#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 17:07:17 2018

@author: wttat
"""

import requests
import json


#获取json格式的数据 info
def Json(seasons,index):
    
    global info
    
    if index == 'Official_Leader':
        url = ('https://stats.nba.com/stats/leagueLeaders?LeagueID=00&'+ \
               'PerMode=PerGame&Scope=S&Season=%s&SeasonType=Regular+Season&StatCategory=PTS') % seasons
               
    elif index == 'Team_General_Traditional':
        url = ('https://stats.nba.com/stats/leaguedashteamstats?Conference=&'+ \
               'DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&'+ \
               'LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&'+ \
               'Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&'+ \
               'PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=%s&'+ \
               'SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&'+ \
               'StarterBench=&TeamID=0&VsConference=&VsDivision=') % seasons
               
    elif index == 'Team_General_Advanced':
        url = ('https://stats.nba.com/stats/leaguedashteamstats?Conference=&'+ \
               'DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&'+ \
               'LeagueID=00&Location=&MeasureType=Advanced&Month=0&OpponentTeamID=0'+ \
               '&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&'+ \
               'PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&'+ \
               'Season=%s&SeasonSegment=&SeasonType=Regular+Season&'+ \
               'ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=') % seasons
               
    elif index == 'Team_General_Scoring':
        url = ('https://stats.nba.com/stats/leaguedashteamstats?Conference=&'+ \
               'DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&'+ \
               'LeagueID=00&Location=&MeasureType=Scoring&Month=0&OpponentTeamID=0&'+ \
               'Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&'+ \
               'PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&'+ \
               'Season=%s&SeasonSegment=&SeasonType=Regular+Season&'+ \
               'ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=') % seasons
               
    elif index == 'Team_General_Defense':
        url = ('https://stats.nba.com/stats/leaguedashteamstats?Conference=&'+ \
               'DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&'+ \
               'LeagueID=00&Location=&MeasureType=Defense&Month=0&OpponentTeamID=0&'+ \
               'Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&'+ \
               'PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&'+ \
               'Season=%s&SeasonSegment=&SeasonType=Regular+Season&'+ \
               'ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=') % seasons
               
    elif index == 'Team_Shooting':
        url = ('https://stats.nba.com/stats/leaguedashteamshotlocations?'+ \
               'Conference=&DateFrom=&DateTo=&DistanceRange=5ft+Range&'+ \
               'Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&'+ \
               'Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&'+ \
               'PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&'+ \
               'PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&'+ \
               'Season=%s&SeasonSegment=&SeasonType=Regular+Season&'+ \
               'ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=') % seasons
    else:
        print ("!@#$!@#$something wrong with the url!@#$!@#$")
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    response = requests.get(url,headers=headers)    
    info = json.loads(response.text)
    print ("fecth jsondata success!")
    return

'''
#测试json文件格式
'''


index = 'Official_Leader'
#index = 'Team_General_Traditional'
#index = 'Team_General_Advanced'
#index = 'Team_General_Scoring'
#index = 'Team_General_Defense'
#index = 'Team_Shooting' #no idea
seasons = '2018-19'
Json(seasons,index)