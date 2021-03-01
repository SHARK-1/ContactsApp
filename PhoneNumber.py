class PhoneNumber:
    '''
    Contains telephone number
    '''

    def __init__(self, number=''):
        self.__number = '+70000000000'
        if number != '':
            self.set_number(number)

    def set_number(self, number):
        number = str(number)
        for char in number:
            int(char)
        if len(number) == 10:
            self.__number = '+7' + number
        else:
            raise ValueError("The number must consist of 10 values, not " + str(len(number)))

    def get_number(self):
        return self.__number

    def del_number(self):
        self.__number = '+70000000000'

    number = property(get_number, set_number, del_number, 'Telephone Number')