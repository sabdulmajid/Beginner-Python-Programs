# Test - 1.py
print('Hello, World!')
x = 'awesome'


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)

print(x)