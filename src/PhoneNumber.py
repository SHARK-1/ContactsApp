import jsonpickle

class PhoneNumber:
    '''
    Contains telephone number
    '''

    def __init__(self, number=''):
        '''
        Phone number object initialization
        :param number: Telephone number. Accepts a number or a string from a number that is 10 characters long, without country code
        '''
        self.__number = '+70000000000'
        if number != '':
            self.set_number(number)

    def set_number(self, number):
        '''
        Setter for telefhone number
        :param number: Accepts a number or a string from a number that is 10 characters long, without country code
        '''
        number = str(number)
        for char in number:
            int(char)
        if len(number) == 10:
            self.__number = '+7' + number
        else:
            raise ValueError("The number must consist of 10 values, not " + str(len(number)))

    def get_number(self):
        '''
        :return: Telephone number
        '''
        return self.__number

    def del_number(self):
        '''
        Sets a default value for a phone number(+70000000000)
        '''
        self.__number = '+70000000000'

    number = property(get_number, set_number, del_number, 'Telephone Number')
