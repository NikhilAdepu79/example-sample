'''
public
private __
protected _

'''

#simple encapsulation 
class demo():
    __a=2 #private 
    _b=4 #protected
    print(__a)
    print(_b)





#other example 
class de():
    def __init__(self,a,b):
        self.__a=a #private
        self._b=b #protected
class de2(de):
    def output(self):
        print(self._b)
d=de2(3,4)
d.output()
# here in this example we can call the protected value 

#here we cannot call the private value 
#simple example for this 
'''class de1():
    def __init__(self,a,b):
        self.__a=a #private
        self._b=b #protected
class de3(de1):
    def output(self):
        print(self.__a)
d=de3(3,4)
d.output()'''

#here we will get the errror if you call the private in encapsulation 


#to correct this and call the private value in the code we will use the get function

class de5():
    def __init__(self, a, b):
        self.__a = a      # private
        self._b = b       # protected

    def get_a(self):     
        return self.__a

class de4(de5):
    def output(self):
        print(self.get_a())  # access via getter
        print(self._b)     # direct access (OK)

d = de4(3, 4)
d.output()
