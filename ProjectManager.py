import jsonpickle


class ProjectManager:
    @staticmethod
    def save(value, file_name='Json.txt'):
        file = open(file_name, mode='w', encoding='Latin-1')
        JSONData = jsonpickle.encode(value)
        file.write(JSONData)

    @staticmethod
    def load(file_name='Json.txt'):
        file = open(file_name, mode='r')
        value = jsonpickle.decode(file.readline())
        file.close()
        return value
