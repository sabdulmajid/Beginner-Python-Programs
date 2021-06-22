# SortingArrays.py
MyList = []
MaxIndex = int(input('Enter the number of indexes:  '))
for k in range(MaxIndex):
    c = int(input('Enter the element: '))
    MyList.append(c)
n = MaxIndex - 1
for i in range(MaxIndex - 1):
    for j in range(n):
        if MyList[j] > MyList[j + 1]:
            Temp = MyList[j]
            MyList[j] = MyList[j + 1]
            MyList[j + 1] = Temp
    n = n - 1
print(MyList)