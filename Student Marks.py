# Student Marks.py
Mark_Array = []
for i in range(15):
    Student_Mark = int(input('Enter a students marks'))
    Mark_Array.append(Student_Mark)

Maximum_Mark = Mark_Array[0]
for i in range(15):
    if Mark_Array[i] > Maximum_Mark:
        Maximum_Mark = Mark_Array[i]
print(f'The maximum mark out of the list is {Maximum_Mark}')

Minimum_Mark = Mark_Array[0]
for i in range(15):
    if Mark_Array[i] < Minimum_Mark:
        Minimum_Mark = Mark_Array[i]
print(f'The minimum mark out of the list is {Minimum_Mark}')

Total_Marks = 0
for i in range(15):
    Total_Marks = Total_Marks + Mark_Array[i]
Average_Marks = Total_Marks/15
print(f'The average mark is {Average_Marks}')

TotalPass = 0
TotalFail = 0
for i in range(15):
    if Mark_Array[i] > 50:
        TotalPass = TotalPass + 1
    else:
        TotalFail = TotalFail + 1
print(f'The total passed students was {TotalPass}')
print(f'The total failed students was {TotalFail}')

