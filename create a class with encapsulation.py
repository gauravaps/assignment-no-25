# write a python sript to update the above profile class with encapsulation.
class student:
    def __init__(self):
        self.__name='gaurav'
        self.__email="gaurav@gmail.com"
        self.__age=25

    def data(self):
        print(self.__name)
        print(self.__email) 
        print(self.__age) 

s1=student()

print(s1.data())          

         
        