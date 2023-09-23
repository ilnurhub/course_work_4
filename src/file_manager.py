from abstract_classes import FileManager
from config import ROOT_PATH, FILENAME
import os
import json


class JSONFileManager(FileManager):
    """
    Класс для работы с json-файлом
    """

    def __init__(self):
        self.filename = FILENAME + '.json'
        self.filepath = os.path.join(ROOT_PATH, 'data', self.filename)

    def write(self, data):
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def read(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            list_of_data = json.load(file)
        return list_of_data

    def delete(self, data):
        list_of_data = self.read()
        list_of_data.remove(data)
        self.write(list_of_data)
