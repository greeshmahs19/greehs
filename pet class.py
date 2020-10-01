class Pet:
    #the __init__method initializes the attributes
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

#mutator method
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age
def main():
    pet = input("enter the name of the pet:")
    a_type = input("enter the type of animal:")
    a_age = input("enter the age of pet:")

#create an instance of book class
    pet_info = Pet(pet, a_type, a_age)
#display data that was entered
    print("here is the data that was entered:")
    print("PET NAME:", pet_info.get_name())
    print("ANIMAL TYPE:", pet_info.get_animal_type())
    print("AGE:", pet_info.get_age())
