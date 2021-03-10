from Contact import Contact


class Project:
    '''
    Contain list of contacts
    '''

    def __init__(self):
        '''
        Create empty contact list
        '''
        self.__contacts = list()

    def add_contact(self, contact):
        '''
        Append contact into contact list
        :param contact: Must be Contact class
        '''
        if isinstance(contact, Contact):
            self.__contacts.insert(0, contact)
            self.__sort()
        else:
            raise ValueError('The contact variable must be an object of the Contact class')

    def del_contact_by_index(self, index):
        '''
        Remove contact from list
        :param index: Contact index in list
        '''
        self.__index_validator(index)
        self.__contacts.pop(index)

    def get_contact(self, index):
        '''
        :param index: Contact index in list
        :return: Contact object
        '''
        self.__index_validator(index)
        return self.__contacts[index]

    def get_all_contacts(self):
        '''
        :return: list of contacts
        '''
        return self.__contacts

    def __index_validator(self, index):
        index = int(index)
        if index < 0 or index >= len(self.__contacts):
            raise IndexError('Incorrect index')

    def __sort(self):
        for i in range(len(self.__contacts) - 1):
            if self.__contacts[i].last_name > self.__contacts[i + 1].last_name:
                self.__contacts[i], self.__contacts[i + 1] = self.__contacts[i + 1], self.__contacts[i]
