from PhoneNumber import PhoneNumber
import datetime


class Contact:
    '''
    В данном классе храниться информацие о человеке.
    Переменные:
    __phone - информация о номере телефона
    __first_name - имя
    __last_name - фамилия
    __age - возраст
    __date_of_birth - дата рождения
    __social_network - социальные сети
    '''

    def __init__(self, number='', firs_name='', last_name='', age=0, date_of_birth=False, social_network=''):
        self.__phone = PhoneNumber(number)
        self.__first_name = ''
        if firs_name != '':
            self.set_first_name(firs_name)
        self.__last_name = ''
        if last_name != '':
            self.set_last_name(last_name)
        self.__age = 0
        if age != 0:
            self.set_age(age)
        self.__date_of_birth = datetime.date(1900, 1, 1)
        if date_of_birth != False:
            self.set_date_of_birth(date_of_birth)
        self.__social_network = ''
        if social_network != '':
            self.set_social_network(social_network)

    def get_phone(self):
        return self.__phone.number

    def set_phone(self, number):
        self.__phone.number = number

    def del_phone(self):
        self.__phone.number = '0000000000'

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        first_name = str(first_name)
        for char in first_name:
            if char == " ":
                raise ValueError('There must be no spaces in the first name')
        if len(first_name) > 50 or len(first_name) == 0:
            raise ValueError('Incorrect length')
        first_name = first_name.lower()
        first_name = first_name.title()
        self.__first_name = first_name

    def del_first_name(self):
        self.__first_name = ''

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        last_name = str(last_name)
        for char in last_name:
            if char == " ":
                raise ValueError('There must be no spaces in the last name')
        if len(last_name) > 50 or len(last_name) == 0:
            raise ValueError('Incorrect length')
        last_name = last_name.lower()
        last_name = last_name.title()
        self.__last_name = last_name

    def del_last_name(self):
        self.__last_name = ''

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date):
        date = datetime.date(date[0], date[1], date[2])
        if date < datetime.date(1900, 1, 1):
            raise ValueError('Date must be greater than 1900')
        if date > datetime.date.today():
            raise ValueError('Date must be less than today')
        self.__date_of_birth = date

    def del_date_of_birth(self):
        self.__date_of_birth = datetime.date(1900, 1, 1)

    def get_social_network(self):
        return self.__social_network

    def set_social_network(self, social_network):
        social_network = str(social_network)
        for char in social_network:
            if char == " ":
                raise ValueError('There must be no spaces in the last name')
        if len(social_network) > 50 or len(social_network) == 0:
            raise ValueError('Incorrect length')
        self.__social_network = social_network

    def del_social_network(self):
        self.__social_network = ''

    def __str__(self):
        return self.__first_name

    phone = property(get_phone, set_phone, del_phone, 'Telephone number')
    first_name = property(get_first_name, set_first_name, del_first_name, 'First name')
    last_name = property(get_last_name, set_last_name, del_last_name, 'Last name')
    date_of_birth = property(get_date_of_birth, set_date_of_birth, del_date_of_birth, 'Date of birthday')
    social_network = property(get_social_network, set_social_network, del_social_network, 'Social network')


if __name__ == '__main__':
    a = Contact('9138510387')
    a.date_of_birth = (2020, 12, 1)
    print(a.date_of_birth)
    # a.date_of_birth = [1998, 125, 3]
    # a.phone = 1234567890
    print(a.phone)
