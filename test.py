#python的类传递的都是指针
class B(object):
    c = 12

class A(object):
    a = B()
    b = 2
    def fun1(self):
        print 'fun1'

    def fun2(self):
        print 'fun2'

def create(a):
    b = A()
    print b
    b.c = 324
    print dir(b)
    print b.c
    d = B()
    d.c = 8
    a.a = d


a = A()
print a.a.c
create(a)
print a.a.c
