# Converting FlowChart - Q2.py
ThreadReject = 0
Count = 1
i = 0
while i != 1:
    if Count != 6:
        if ThreadReject <= 1:
            print('Car is potentially roadworthy.')
        else:
            print('Car is not roadworthy.')
        i = i + 1
    else:
        Depth = float(input('Enter a depth: '))
        if Depth <= 1.6:
            ThreadReject = ThreadReject + 1
        else:
            Count = Count + 1
