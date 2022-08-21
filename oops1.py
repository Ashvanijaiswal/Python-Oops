class Student:
    '''This is wriiten by me as a string documnentation'''
    def __init__(self):
        self.name='ashvani'
        self.age=48
        self.marks=80

    def talk(self):
        print("hello i m: ",self.name)
        print("my age is : ",self.age)
        print("My marks :",self.marks)
    

s=Student()
s.talk()