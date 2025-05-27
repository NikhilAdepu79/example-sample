'''
def function.name():
        function bidy 
    function.name()

'''

def add(a,b):
    return a+b
print(add(1,2)) #simple function

#nested function

def outer():
    print('outer')
    def inner():
        print('inner')
    inner()
outer()



#function call 
def fuin():
    print('this is nikhil')
fuin()
fuin()


def funi(*a):
    print('this is nikhil',a)
funi()
funi(1,2,3) 




#keyword argument

def fun(**a):
    print('nikhil',a)
fun(a=1,b=3) #it will store in the dict



