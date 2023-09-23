from abstract_classes import FileManager
from config import ROOT_PATH, FILENAME
import os


class JSONFileManager(FileManager):
    """
    Класс для работы с json-файлом
    """

    def __init__(self):
        self.filename = FILENAME + '.json'
        self.filepath = os.path.join(ROOT_PATH, 'data', self.filename)

    def write(self, data):
        pass

    def read(self):
        pass

    def delete(self):
        pass
