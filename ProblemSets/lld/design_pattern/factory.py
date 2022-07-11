__doc__ = """
FACTORY DESIGN PATTERN \n
The idea is to create an object of a child class on runtime.
"""
from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def person_method():
        """Interface method"""

class Student(IPerson):
    def __init__(self) -> None:
        self.name = "Base student method"
    
    def person_method(self):
        print("I'm a student")

class Teacher(IPerson):
    def __init__(self) -> None:
        self.name = "Basic Teacher method"
    
    def person_method(self):
        print("I'm a teacher")

def main(input_type):
    """
    Strategy 1
    """
    factory_config = {
        "teacher": Teacher(),
        "studnet": Student()
    }
    return factory_config[input_type]

def main_2(input_type):
    """
    Old school if else check
    """
    if input_type == "teacher":
        return Teacher()
    elif input_type == "student":
        return Student()

if __name__ == "__main__":
    obj = main(input_type="teacher")
    obj.person_method()