#Recursion means a function calling itself again and again until a condition is met (base case).

#simple example
def show(n):
    if n > 5:
        return
    print(n)
    show(n + 1)

show(1)


#factorial function in python 
def factor(n):
    if n == 0 or n == 1:
        return 1
    return n * factor(n - 1)

print(factor(6))


'''
Recursive Structure
Every recursive function needs:

Base Case – When to stop

Recursive Call – Function calls itself

'''
