from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_data():
        """Implement in child class"""


class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            return PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance
    
    def __init__(self, name, age) -> None:
        if PersonSingleton.__instance != None:
            raise Exception("Singleton can't be instantiated")
        else:
            self.name = name
            self.age = age 
            PersonSingleton.__instance = self
    
    def set_name(self, name):
        self.name = name
    
    @staticmethod
    def get_data():
        print(f"Name: {PersonSingleton.__instance.name}")

if __name__ == "__main__":
    obj = PersonSingleton("Akshay", 27)
    obj.get_data()

    obj2 = obj.get_instance()
    obj2.set_name("Swayam")
    obj2.get_data()
    