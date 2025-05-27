'''
there are 4 types 
single inheritance - parent to child
mulitlevel inhertitance - grand father , father , child
mulitple inheritance - mother , father , child
hierarchiral inheritance - father , child1 ,child2




'''



#single inheritance
class parents():
    def outputs(self):
        print("i am parent")
class childs(parents):
    def output(self):
        print('i am child')
c=childs()
c.output()
c.outputs()




#mulitlevel inheritance

class grandparent():
    def outputgf(self):
        print("i am grandparent")
class parent(grandparent):
    def outputp(self):
        print('i am parent')
class child(parent):
    def outputc(self):
        print('i am child')
c=child()
c.outputc()
c.outputp()
c.outputgf()


#mulitple inheritance

class father():
    def outputf(self):
        print('i am father')
class mother():
    def outputm(self):
        print("i am mother")
class childcc(father,mother):
    def outputcc(self):
        print("i am child of them")
c=childcc()
c.outputm()
c.outputf()
c.outputcc()





#hierariactral inheritance


class prinicipal():
    def outputp(self):
        print('am prinipal')
class child1(prinicipal):
    def outputccc(self):
        print('i am the child 1')
class child2(prinicipal):
    def outputcccc(self):
        print('i am the child 2')
c1=child1()
c2=child2()
#n.outputp()
c1.outputccc()
c1.outputp()
c2.outputcccc()
c2.outputp()
#n1.outputp()c1.output2()