from io import FileIO
import json

treatedDataFile = "./Ressources/treatedData.json"
treatedFileFile = "./Ressources/treatedFile.json"


def loadData(file):
    with open(file) as json_file:
        data = json.load(json_file)
        return data

        def saveData(dict, file):
    data_file = open(file, "w")
    json.dump(dict, data_file)
    data_file.close()

    def readFile(filePath):
        with open(filePath) as fileObj:
            CanStartReading = False
            line = fileObj.read(1)