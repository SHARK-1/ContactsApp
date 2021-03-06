import jsonpickle
import os


class ProjectManager:
    @staticmethod
    def save(value, file_name='Json.txt'):
        if os.path.isfile(file_name):
            os.remove(file_name)
        file = open(file_name, mode='w', encoding='Latin-1')
        JSONData = jsonpickle.encode(value)
        file.write(JSONData)

    @staticmethod
    def load(file_name='Json.txt'):
        if os.path.isfile(file_name):
            file = open(file_name, mode='r')
            value = jsonpickle.decode(file.readline())
            file.close()
            return value
        else:
            raise BaseException('file not found')
