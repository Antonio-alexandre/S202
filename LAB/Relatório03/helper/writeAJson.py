import json
import os
from bson import json_util 


def writeAJson(data, name: str):
    parsed_json = json.loads(json_util.dumps(data))

    if not os.path.isdir("./LAB/Relatório03/json"):
        os.makedirs("./LAB/Relatório03/json")
        
    with open(f"./LAB/Relatório03/json/{name}.json", 'w') as json_file:
        json.dump(parsed_json, json_file,
                  indent=4,
                  separators=(',', ': '))