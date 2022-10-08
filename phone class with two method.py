# write a python script to create a phone class with 2 method to print the features (calind
# and sms)

class phone:
    def calling(self ,call):
        self.cal=call
        return self.cal

    def msg(self,sms):
        self.message=sms
        return self.message   

s1=phone()
print(s1.calling("please call"))  
print(s1.msg("sending msg"))      
