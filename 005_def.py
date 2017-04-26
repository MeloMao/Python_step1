#coding=utf-8

def test(x):
    x=888
    return x

def test1(x):
    y=999
    return y

def change(x):
    x[0]=8
    return x

print test(2)
print test1(2)
x=[1,2,3]
print x
print change(x)
