"""
Created on Sat Nov 10 14:25:18 2018
Github : https://github.com/wtttat/NBA_STAT_BIG_DATA/
@author: wttat
"""
import requests
import json
import csv
import datetime
import os

"""
#生成赛季范围 1996-97 etc
#真的好麻烦啊
"""
oldest_year = 1996
current_year = datetime.datetime.now().year #当前年份
season_range_int = [s for s in range(oldest_year+1,current_year+2)]
year_range_int = [y for y in range(oldest_year,current_year+1)]
year_range = [str(y) for y in year_range_int]
season_range = [str(y) for y in season_range_int]
endyear =  [s[-2:] for s in season_range] #截断后两位
year_length = len(season_range_int)
season = [s for s in range(year_length)]
for i in range(year_length): #拼接
    season[i] = year_range[i]+"-"+endyear[i]


#网上找的生成目录的函数
def mkdir(path):

    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print (path+' 创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path+' 目录已存在')
        return False

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

#生成行名称 RowName
def GetRowName(index):
    
    global RowName
    
    if index == 'Official_Leader':
        
        RowName = [r for r in info["resultSet"]["headers"]]
        
        '''
        RowName = ["ID","RANK","NAME","TEAM","Games Played","Minutes Played","Field Goals Made",
                   "Field Goals Attempted","Field Goal Percentage","3 Point Field Goals Made",
                   "3 Point Field Goals Attempted","3 Point Field Goals Percentage","Free Throws Made",
                   "Free Throws Attempted","Free Throw Percentage","Offensive Rebounds","Defensive Rebounds",
                   "Defensive Rebounds","Assists","Steals","Blocks","Turnovers","Points","Efficiency"]
        '''
        
    elif index == 'Team_General_Traditional' or 'Team_General_Advanced' or 'Team_General_Scoring' or 'Team_General_Defense':
        RowName = [r for r in info["resultSets"][0]["headers"]]
    
    elif index == 'Team_Shooting':
        RowName = [r for r in info["resultSets"]["headers"]]
        
    else:
        print ("!@#$!@#$something wrong with the rowname@#$!@#$")
    print ("fetch rowname success!")
    return


'''
#将数据转换成csv格式
'''
def getData(seasons,index):
    
    path = ("./%s") % index
    mkdir(path)
    csvpath = ("./%s/%s.csv") % (index,seasons)
    
    Json(seasons,index)
    GetRowName(index)
    
    #testrowname = [for r in info["resultSet"]]
    
    #写入对应的csv
    with open(csvpath,"w",newline="") as csvfile:
        writer = csv.writer(csvfile,dialect="excel")        
        writer.writerow(RowName)
        
        if index == 'Official_Leader':
            for row in info["resultSet"]["rowSet"]:
                writer.writerow(row)
        elif index == 'Team_General_Traditional' or 'Team_General_Advanced' or 'Team_General_Scoring' or 'Team_General_Defense':
            for row in info["resultSets"][0]["rowSet"]:
                writer.writerow(row)
        elif index == 'Team_Shooting': # for fix
            for row in info["resultSets"]["rowSet"]:
                writer.writerow(row)
        else:
            print("!@#$@!#something wrong with the index!@#!@#!@#")
        
        csvfile.close()
    print("%s %s season data get~" %(index,seasons))

'''
#dead code
#index = 'Official_Leader'
#index = 'Team_General_Traditional'
#index = 'Team_General_Advanced'
#index = 'Team_General_Scoring'
#index = 'Team_General_Defense'
#index = 'Team_Shooting'
index = ["Official_Leader","Team_General_Traditional","Team_General_Advanced",
         "Team_General_Scoring","Team_General_Defense","Team_Shooting"]
'''



'''
索引数组
'''
index = ["Official_Leader","Team_General_Traditional","Team_General_Advanced",
         "Team_General_Scoring","Team_General_Defense"]

'''
#主函数
#赛季取1996-97至最新
'''

begin = datetime.datetime.now()

for i in index:
    for s in season:
        start = datetime.datetime.now()
        getData(s,i)
        end = datetime.datetime.now()
        print (end - start)
        
done = datetime.datetime.now()
print (done - begin)

