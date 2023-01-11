# global_local_scope.py
a = 5

def foo():
    print(a) # local scope에 a가 없네?

foo()

a = 5

def boo():
    global a
    a = 3
    print(a)

boo()
print(a)