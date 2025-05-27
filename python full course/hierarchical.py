# Hierarchical Inheritance Example

class Principal:
    def outputp(self):
        print('I am the principal')

class Child1(Principal):
    def output1(self):
        print('I am Child 1')

class Child2(Principal):
    def output2(self):
        print('I am Child 2')

# Create objects of both child classes
c1 = Child1()
c2 = Child2()

# Call parent and child methods
c1.outputp()
c1.output1()

c2.outputp()
c2.output2()
