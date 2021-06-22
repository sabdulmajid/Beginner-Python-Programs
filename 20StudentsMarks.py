# 20StudentsMarks.py
Mark_Array = []
for i in range(20):
    Student_Mark = int(input('Enter a students marks   '))
    Mark_Array.append(Student_Mark)

Total_Marks = 0
for i in range(20):
    Total_Marks = Total_Marks + Mark_Array[i]
Average_Marks = Total_Marks / 20
print(f'\nThe class average mark is {Average_Marks}')

TopGrade = 0
SecondGrade = 0
ThirdGrade = 0
FourthGrade = 0
LastGrade = 0
for i in range(20):
    if 50 <= Mark_Array[i] < 60:
        LastGrade = LastGrade + 1
    elif 60 <= Mark_Array[i] < 70:
        FourthGrade = FourthGrade + 1
    elif 70 <= Mark_Array[i] < 80:
        ThirdGrade = ThirdGrade + 1
    elif 80 <= Mark_Array[i] < 90:
        SecondGrade = SecondGrade + 1
    elif 90 <= Mark_Array[i]:
        TopGrade = TopGrade + 1
print(f'\nTotal A* grades are {TopGrade}')
print(f'Total A grades are {SecondGrade}')
print(f'Total B grades are {ThirdGrade}')
print(f'Total C grades are {FourthGrade}')
print(f'Total D grades are {LastGrade}')

TotalPass = 0
TotalFail = 0
for i in range(20):
    if Mark_Array[i] > 50:
        TotalPass = TotalPass + 1
    else:
        TotalFail = TotalFail + 1
print(f'\nThe total failed students was {TotalFail}')
print(f'The total passed students was {TotalPass}')

HighestMarks = 0
for i in range(20):
    if Mark_Array[i] > HighestMarks:
        HighestMarks = Mark_Array[i]
print(f'\nThe highest marks was {HighestMarks}')

LowestMarks = Mark_Array[0]
for i in range(20):
    if Mark_Array[i] < LowestMarks:
        LowestMarks = Mark_Array[i]
print(f'The lowest marks was {LowestMarks}')
