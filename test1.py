
class User:
    def __init__(self, name, age):
        self.__name = name
        self._age = age

    def _get_name(self):
        return self.__name
    

class Student(User):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self._course = course

    def _get_course(self):
        return self._course
    
    def _get_age(self):
        return self._age

userData = {
    'name': "Mark Gaje",
    'age': 23,
    'course': "BSIT"
}

user = Student(**userData)

print(user._get_name())
print(user._get_age())