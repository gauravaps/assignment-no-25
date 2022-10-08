# create a class method and access i


class student:
    school="mbbs"
    def __init__(self):
        self.marks=50
    @classmethod
    def f1(self):
       return self.school

    #@classmethod
    #def schl(self):
     #   return self.school   


s1=student()

print(s1.marks)
print(student.f1())

      