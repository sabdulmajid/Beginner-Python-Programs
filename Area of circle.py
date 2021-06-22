def area(r):
     a = 3.14159 * r**2
     return a

radius = int(input('Enter a radius of a circle, for which the area will be given '))

area = area(radius)
print('The area of your circle is', area, 'cm**2')


#Separate function
             
def my_function():
     return 1, 2

b, a = my_function()

print(a)
print(b)

def greeting():
     print('Hello Hello Hello')

greeting()

def dead_end():
     print('I am sorry, you can go no further this way!')

dead_end()

def highest_mark():
     print('You are a genius! You got the highest marks in class!')
     
highest_mark()