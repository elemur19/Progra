import json
import csv


# La clase FileConverter implementada como Singleton 
class FileConverter:

    _instance = None   

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FileConverter, cls).__new__(cls)
        return cls._instance

# Leer el archivo JSON:
    def convertFromJson(self, jsonFileStr):

        with open(jsonFileStr, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data

# Leer el arhivo CSV:
    def convertFromCSV(self, csvFileStr):

        data = []

        with open(csvFileStr, 'r', encoding='utf-8') as file:

            reader = csv.DictReader(file)

            for row in reader:
                data.append(dict(row))

        return data