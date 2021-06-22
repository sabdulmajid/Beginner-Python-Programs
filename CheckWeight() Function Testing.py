# Checkweight().py

MaxWeight = 100
Threshold = 5
BarWeight = [123, 122, 1222, 922, 1110, 1092]

counter = 0
for i in BarWeight:
    if i > MaxWeight:
        counter += 1
if counter > Threshold:
    print('ServiceCheck()')
elif counter <= Threshold:
    print(f'ShippingBox OK - Maximum Threshold Weight Exceeded {counter} times.')