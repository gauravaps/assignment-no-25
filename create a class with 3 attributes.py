# write a python script to create a profile with 3 attributes (name,email,age).

class student:
    def __init__(self):
        self.name="gaurav"
        self.email="gaurav@gmail.com"
        self.age=25
    def data(self):
        print("name =" ,self.name)
        print("email =", self.email)
        print("age =", self.age)

s1=student()
print(s1.data())            
        