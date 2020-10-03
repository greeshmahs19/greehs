class Personal_info:
    def __init__(self, name, age, address, ph_num):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__ph_num = ph_num

    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    def set_address(self, address):
        self.__address = address
    def set_ph_num(self, ph_num):
        self.__ph_num = ph_num

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_address(self):
        return self.__address
    def get_ph_num(self):
        return self.__ph_num
    def __str__(self):
        return 'Name: ' + self.__name + '\n' +\
               'Age: ' + self.__age + '\n' +\
               'Address: ' + self.__address + '\n' +\
               'Phone num: ' + self.__ph_num

gree = Personal_info('Greeshma hs', '22', '25, parimalanagar, arshinkunte', '8975412568')
vis = Personal_info('vismaya', '21', 'kanvanagar, nelmangala', '835564568')
rah = Personal_info('Rahul', '12', 'chikbanavara, abbigere', '784512369')

print(gree, end = '\n\n')
print(vis, end = '\n\n')
print(rah, end = '\n\n')

 
    
