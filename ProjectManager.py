import jsonpickle
import os, getpass


class ProjectManager:
    __FILENAME = f'C:\\Users\\{getpass.getuser()}\\Documents\\ContactsApp.notes'

    @staticmethod
    def save(value, file_name=__FILENAME):
        '''
        Save contacts
        :param value:Contact list
        :param file_name: File name
        :return:
        '''
        if os.path.isfile(file_name):
            os.remove(file_name)
        file = open(file_name, mode='w', encoding='Latin-1')
        JSONData = jsonpickle.encode(value)
        file.write(JSONData)

    @staticmethod
    def load(file_name=__FILENAME):
        '''
        Load Contacts
        :param file_name: File name
        :return:
        '''
        if os.path.isfile(file_name):
            file = open(file_name, mode='r')
            value = jsonpickle.decode(file.readline())
            file.close()
            return value
        else:
            raise BaseException('file not found')
