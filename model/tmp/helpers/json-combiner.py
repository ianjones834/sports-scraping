import json_covert
import json

files = ['mlb', 'nba', 'ncaaf', 'nfl', 'nhl']

allDataDict = dict()

for file in files:
  newSportDict = json_covert.jsonConvert(file)
  allDataDict.update({file: newSportDict})

with open('./data/data.json', 'w') as dataFile:
  dataFile.write(json.dumps(allDataDict))

print("\nDone Processing Data!\nData JSON located at ./data/data.json")