# create a python script to create a calculator 2.0 and inharit first calculator class  .


class calculator:
    @staticmethod
    def add(num1,num2):
        return num1+num2,num1*num2
class calcutalot2(calculator):
    def multi(num3,num4):
        return num3+num4


# s1=calculator()
s1=calcutalot2()
print(calculator.add(8,9))
print(calcutalot2.multi(5,5))

