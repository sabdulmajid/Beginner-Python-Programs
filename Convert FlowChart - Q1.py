# Convert FlowChart - Q1.py
Senior = 0
Adult = 0
Child = 0
Z = 0
i = 1
while i == 1:
    Type = input('''Enter a letter from the list: 
    S for Senior
    A for Adult
    C for Child
    Z to end the program. 
    ''')
    if Type == 'S':
        print('Input Accepted')
        Senior = Senior + 1
    elif Type == 'A':
        print('Input Accepted')
        Adult = Adult + 1
    elif Type == 'C':
        print('Input Accepted')
        Child = Child + 1
    elif Type == 'Z':
        Z = Z + 1
    else:
        print('Not accepted')
    if Z == 1:
        break

print('Number of Senior(s):', Senior)
print('Number of Adult(s):', Adult)
print('Number of Child(ren):', Child)
