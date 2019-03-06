def cleanString(str):
    return str.replace('Ticket Info','').replace('Match Guide','').replace('Girls Fantasy Camp','').replace('|','').replace('Buy Tickets','').strip().replace('\n', ' ').replace('\r', '')

def replaceSponsor(str):
    import re
    return re.sub(r', Presented(.)+','',str)

def getUSTeam(team):
    return team[0 : team.find("vs")].strip()

def getOpponentTeam(team):
    if(team.find("-") < 5):
        return team[team.find("vs"):].strip()[3:]
    
    return team[team.find("vs") : team.find("-")].strip()[3:]

def getCompetition(team):
    if(team.find("-") < 5 ):
        return ""
    index = max([i for i, ltr in enumerate(team) if ltr == "-"])
    return team[index : ].strip()[2:]

def getScoreArray(str):
    import re
    return re.findall(r'\d+', str)
