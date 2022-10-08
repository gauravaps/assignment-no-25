#encapsulation class

class student:
    def  __init__(self):
        self.age=None
        self.name=None

    def getage(self):
        return self.age ,self.name

    def setage(self ,age,name) :
        self.age = age 
        self.name=name


s1=student()
s1.setage(250,'gaurav')
print(s1.getage())               