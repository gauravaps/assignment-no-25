# write a python script to create an application like truecaller where names and numbers are 
#stored.truecaller class will have 2 method ( 1st to fetch the name of  number 2nd  to add a new
#  entry).

class truecaller:
    def name(self,n):
        self.n1=n
        return self.n1



class phone(truecaller):
    def number(self):
        print("number is 8319271749")





s1=truecaller()
s2=phone()
print(s1.name())
print(s1.number())