'''
if 
else 
elif 
nested if 

'''


#if 
#if expression :
#statement to be exceuted 

a=10
b=200
if b>a:
    print("b is greater than a ")


'''
if else 

if condition:
    code block to run if the condition is true 
else:
    code block to run if condition is false

'''

age=17
if age>=18:
    print('he can vote')

else:
    print('he is not eligible')


'''
elif statement

if condition:
    code block to be excuted of condtion is true
elif another condiiton:
    code block to be excuted of the condition is true 
else:
    code block to execute if all the above condition are false 

'''


x=10
if x<0:
    print('+ve')
elif x==0:
    print('zero')
else:
    print('-ve')



'''
nested if 

if condition 1:
    code block 1 
    if condition 2:
        code block 2
    else:
        coddde block 3
else:
    code block 4
'''

num=10
if num>0:
    print('+ves')
    if num%2==0:
            print('even no. ')
    else:
            print('odd')
else:
    print('-ves')