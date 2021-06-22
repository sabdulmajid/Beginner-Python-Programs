# Functions_While Loop
def largest():
    a = int(input('Enter the first of the 3 numbers:  '))
    b = int(input('Enter the second of the 3 numbers:  '))
    c = int(input('Enter the last of the 3 numbers:  '))
    if a > b and a > c:
        print(f'The largest element is {a}')
    elif b > a and b > c:
        print(f'The largest element is {b}')
    else:
        print(f'The largest element is {c}')

def studentresult():
    Mark_Array = []
    for i in range(5):
        Student_Mark = int(input('Enter a students marks'))
        Mark_Array.append(Student_Mark)

    Total_Marks = 0
    for i in range(5):
        Total_Marks = Total_Marks + Mark_Array[i]
    Average_Marks = Total_Marks / 5
    print(f'The average mark is {Average_Marks}')

    Percentage = 1
    for i in range(5):
        Percentage = Average_Marks
    print('The percentage is', Percentage,'%')

i = 1
while i == 1:
    choice = input("""1 -----> Largest of 3 numbers
2 -----> Student Results
3 -----> Exit
    Enter your choice:  """)

    if choice == '1':
        largest()
    elif choice == '2':
        studentresult()
    else:
        i = 0
