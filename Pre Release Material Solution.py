# Pre Release Material Solution.py
PhoneDescriptionArray = ['Compact',
                         'Clam Shell',
                         'RoboPhone - 5-inch screen and 64GB memory',
                         'RoboPhone - 6-inch screen and 256GB memory',
                         'Y-Phone Standard - 6-inch screen and 64GB memory',
                         'Y-Phone Standard - 6-inch screen and 256GB memory']
PhoneItemCodeArray = ['BPCM', 'BPSH', 'RPSS', 'RPLL', 'YPLS', 'YPLL']
PhonePriceArray = [29.99, 49.99, 199.99, 499.99, 549.99, 649.99]


TabletItemCodeArray = ['RTMS', 'RTLM', 'YTLM', 'YTLL']
TabletDescriptionArray = ['RoboTab - 8-inch screen and 64GB memory',
                      'RoboTab - 10-inch screen and 128GB memory',
                      'Y-Tab Standard - 10-inch screen and 128GB memory',
                      'Y-Tab Deluxe- 10-inch screen and 256GB memory']
TabletPriceArray = [149.99, 299.99, 499.99, 599.99]


SIMCardItem = ['SMNO', 'SMPG']
SIMCardDescriptionArray = ['SIM Free (no SIM card purchased)', 'Pay As You Go (SIM card purchased)']
SIMCardPriceArray = [0.00, 9.99]


CaseItemCodeArray=['CSST', 'CSLX']
CaseDescriptionArray = ['Standard', 'Luxury']
CasePriceArray = [0.00, 50.00]


ChargerItemArray = ['CGCR', 'CGHM']
ChargerDescriptionArray = ['Car', 'House']
ChargerPriceArray = [19.99, 15.99]

TotalPrice = 0
Counter = 0
ItemList = []

while True:
    Choice = int(input('Please choose a phone or tablet. For Phone, type 1 and for Tablet, type 2:  '))
    if Choice == 1:
        print(
            f'1. Phone Code:{PhoneItemCodeArray[0]}, Description:{PhoneDescriptionArray[0]}, Price: ${PhonePriceArray}')
        print(
            f'2. Phone Code:{PhoneItemCodeArray[0]}, Description:{PhoneDescriptionArray[0]}, Price: ${PhonePriceArray}')
        print(
            f'3. Phone Code:{PhoneItemCodeArray[0]}, Description:{PhoneDescriptionArray[0]}, Price: ${PhonePriceArray}')
        print(
            f'4. Phone Code:{PhoneItemCodeArray[0]}, Description:{PhoneDescriptionArray[0]}, Price: ${PhonePriceArray}')
        print(
            f'5. Phone Code:{PhoneItemCodeArray[0]}, Description:{PhoneDescriptionArray[0]}, Price: ${PhonePriceArray}')
        print(
            f'6. Phone Code:{PhoneItemCodeArray[0]}, Description:{PhoneDescriptionArray[0]}, Price: ${PhonePriceArray}')
        PhoneType = int(input('Type a number between 1-6 to chose the phone you wantto buy:  '))
        if PhoneType == 1:
            TotalPrice = TotalPrice + PhonePriceArray[0]
        elif PhoneType == 2:
            TotalPrice = TotalPrice + PhonePriceArray[1]
        elif PhoneType == 3:
            TotalPrice = TotalPrice + PhonePriceArray[3]
        elif PhoneType == 4:
                TotalPrice = TotalPrice + PhonePriceArray[4]
        elif PhoneType == 5:
            TotalPrice = TotalPrice + PhonePriceArray[5]
        elif PhoneType == 6:
            TotalPrice = TotalPrice + PhonePriceArray[6]
