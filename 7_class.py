class Melo():
    def __init__(self):
        print'If this sentence come out then the program is right'

    def add(self,x):#There must define a self
        x=x+1
        return x

x=2
print '2+1='+repr(Melo().add(x))#'repr' can change int to string
