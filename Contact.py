from PhoneNumber import PhoneNumber
import datetime


class Contact:
    '''
    Contains contact details
    '''

    def __init__(self, number='', firs_name='', last_name='', age=0, date_of_birth=[1900, 1, 1], email='',
                 social_network=''):
        self.__phone = PhoneNumber(number)
        self.__first_name = ''
        if firs_name != '':
            self.set_first_name(firs_name)
        self.__last_name = ''
        if last_name != '':
            self.set_last_name(last_name)
        self.__date_of_birth = datetime.date(1900, 1, 1)
        if date_of_birth != [1900, 1, 1]:
            self.set_date_of_birth(date_of_birth)
        self.__social_network = ''
        if social_network != '':
            self.set_social_network(social_network)
        self.__email = ''
        if email != '':
            self.set_email(email)

    def get_phone(self):
        return self.__phone.number

    def set_phone(self, number):
        '''
        :param number: Length of number - 10
        '''
        self.__phone.number = number

    def del_phone(self):
        self.__phone.number = '0000000000'

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__length_validator(first_name, 'first name')
        first_name = first_name.lower()
        first_name = first_name.title()
        self.__first_name = first_name

    def del_first_name(self):
        self.__first_name = ''

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__length_validator(last_name, 'last name')
        last_name = last_name.lower()
        last_name = last_name.title()
        self.__last_name = last_name

    def del_last_name(self):
        self.__last_name = ''

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date):
        '''
        :param date: Date format: int array [year,month,day]
        '''
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
        self.__length_validator(social_network, 'social network')
        self.__social_network = social_network

    def del_social_network(self):
        self.__social_network = ''

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__length_validator(email, 'email')
        self.__email = email

    def del_email(self):
        self.__email = ''

    def __str__(self):
        return self.__first_name

    def __length_validator(self, value, name):
        '''
        Checks the correctness of a string variable
        for spaces and length
        :param name: field name
        :return:
        '''
        value = str(value)
        for char in value:
            if char == " ":
                raise ValueError(f'There must be no spaces in the {name}')
        if len(value) > 50 or len(value) == 0:
            raise ValueError('Incorrect length')

    phone = property(get_phone, set_phone, del_phone, 'Telephone number')
    first_name = property(get_first_name, set_first_name, del_first_name, 'First name')
    last_name = property(get_last_name, set_last_name, del_last_name, 'Last name')
    date_of_birth = property(get_date_of_birth, set_date_of_birth, del_date_of_birth, 'Date of birthday')
    social_network = property(get_social_network, set_social_network, del_social_network, 'Social network')
    email = property(get_email, set_email, del_email, 'E-Mail')