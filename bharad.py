import requests
import json
import csv

class Player(object):
    fName = ""
    sName = ""
    news = ""
    tout = 0
    tin = 0
    bps = 0
    threat = 0
    total_points = 0

    def __init__(self, fName, sName, team_code, element_type, squad_number):
        self.fName = fName
        self.sName = sName
        self.team_code = team_code
        self.element_type = element_type
        self.squad_number = squad_number

    def __str__(self):
        toRet = "{} {}\n{}\n{}\n{}\n".format(self.fName, self.sName, self.team_code, self.squad_number, self.element_type)
        return toRet

def toUTF8(s):
    return unicode(s).encode("utf-8")

def create_csv(list):
    ret = []
    ret.append([toUTF8("First Name"), toUTF8("Second Name"), toUTF8("Team Name"), toUTF8("Position"), toUTF8("Squad Number")])
    for item in list:
        lis = []
        lis.append(toUTF8(item.fName))
        lis.append(toUTF8(item.sName))
        lis.append(toUTF8(item.team_code))
        lis.append(toUTF8(item.element_type))
        lis.append(toUTF8(item.squad_number))
        ret.append(lis)
    return ret

def position_name(element_type):
    if element_type==1:
        return "GKP"
    elif element_type==2:
        return "DEF"
    elif element_type==3:
        return "MID"
    elif element_type==4:
        return "FWD"
    else:
        return "ERROR"

def team_name(team_code):
    if team_code==3:
        return "Arsenal"
    elif team_code==91:
        return "Bournemouth"
    elif team_code==36:
        return "Brighton"
    elif team_code==90:
        return "Burnley"
    elif team_code==97:
        return "Cardiff"
    elif team_code==8:
        return "Chelsea"
    elif team_code==31:
        return "Crystal Palace"
    elif team_code==11:
        return "Everton"
    elif team_code==54:
        return "Fulham"
    elif team_code==38:
        return "Huddersfield"
    elif team_code==13:
        return "Leicester"
    elif team_code==14:
        return "Liverpool"
    elif team_code==43:
        return "Man City"
    elif team_code==1:
        return "Man Utd"
    elif team_code==4:
        return "Newcastle"
    elif team_code==20:
        return "Southampton"
    elif team_code==6:
        return "Spurs"
    elif team_code==57:
        return "Watford"
    elif team_code==21:
        return "West Ham"
    elif team_code==39:
        return "Wolves"
    else:
        return "ERROR"


resp = requests.get('https://fantasy.premierleague.com/drf/bootstrap-static')
if resp.status_code != 200:
    print "Failed"
else:
    js = resp.json()
    ele = js['elements']
    lis = []
    # print ele[0]
    for item in ele:
        play = Player(item['first_name'], item['second_name'], team_name(item['team_code']), position_name(item['element_type']), item['squad_number'])
        lis.append(play)

    # lis.sort(key=lambda x: x.form, reverse=True)
    # print lis[0]
    # for i in lis:
    #     print i

    toCSV = create_csv(lis)
    # print toCSV

    myFile = open('bharad.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(toCSV)
    print("Writing complete")

