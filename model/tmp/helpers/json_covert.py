import json

def jsonConvert(file):
  with open("tmp/" + file + ".jsonl", 'r') as sportData:
    sportDataList = list(sportData)

  sportDict = dict()

  for team in sportDataList:
    curTeam = json.loads(team)
    sportDict.update({curTeam['team']: {'ml': curTeam['ml'], 'bpi': curTeam['bpi'],}})

  return sportDict