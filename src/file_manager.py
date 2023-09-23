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
        pass

    def delete(self, data):
        pass
