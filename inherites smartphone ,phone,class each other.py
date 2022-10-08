# write a python script to create a smartphone class by inherites calculator 2.0and phone class

class phone:
    def calling(self ,call):
        self.cal=call
        return self.cal

class smartphone(phone):
    def iphone(self):

        print("smartphone iphone 13")


class calculator(smartphone):
    @staticmethod
    def add(num1,num2):
        return num1+num2          

#s1=phone()
#s2=smartphone()
s3=calculator()
print(s3.calling("calling here"))
print(s3.iphone())  
print(calculator.add(8,8))     
