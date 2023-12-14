import os
import json

from data_structures.liste import chained_list

def saveExist(path):
    if os.path.isfile(path):
        print("user has a save file")
        file = open(path,"r+")
        data = json.load(file)
    else:
        print("user doesnt have a save file")
        file = open(path,"w")
        file.write('{"history":[]}')
        data = json.loads('{"history":[]}')
    return data

def saveImport(data):
    cl = chained_list()
    for d in data["history"]:
        cl.append(d)
    return cl
    
def saveExport(data,historique,file):
    historiqueJSON='['
    h=""
    for i in range(historique.lenght()):
        if i < historique.lenght()-1:
            h+='"'+str(historique.get(i))+'", '
        else:
            h+='"'+str(historique.get(i))+'"'
    historiqueJSON+=h+']'
    data['history'] = json.loads(historiqueJSON)
    file.seek(0)
    json.dump(data, file, indent=4)
    file.truncate()