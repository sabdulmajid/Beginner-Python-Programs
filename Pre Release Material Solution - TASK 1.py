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


SIMCardItemCodeArray = ['SMNO', 'SMPG']
SIMCardDescriptionArray = ['SIM Free (no SIM card purchased)', 'Pay As You Go (SIM card purchased)']
SIMCardPriceArray = [0.00, 9.99]


CaseItemCodeArray = ['CSST', 'CSLX']
CaseDescriptionArray = ['Standard', 'Luxury']
CasePriceArray = [0.00, 50.00]


ChargerItemCodeArray = ['CGCR', 'CGHM']
ChargerDescriptionArray = ['Car', 'House']
ChargerPriceArray = [19.99, 15.99]

TotalPrice = 0
Counter = 0
ItemListArray = []

while Counter == 0:
    Choice = int(input('Please choose a phone or tablet. For a phone, type 1 and for a tablet, type 2:  '))

    if Choice == 1:
        print(
            f'1. Phone Code: {PhoneItemCodeArray[0]}, Description: {PhoneDescriptionArray[0]}, Price: ${PhonePriceArray[0]}')
        print(
            f'2. Phone Code: {PhoneItemCodeArray[1]}, Description: {PhoneDescriptionArray[1]}, Price: ${PhonePriceArray[1]}')
        print(
            f'3. Phone Code: {PhoneItemCodeArray[2]}, Description: {PhoneDescriptionArray[2]}, Price: ${PhonePriceArray[2]}')
        print(
            f'4. Phone Code: {PhoneItemCodeArray[3]}, Description: {PhoneDescriptionArray[3]}, Price: ${PhonePriceArray[3]}')
        print(
            f'5. Phone Code: {PhoneItemCodeArray[4]}, Description: {PhoneDescriptionArray[4]}, Price: ${PhonePriceArray[4]}')
        print(
            f'6. Phone Code: {PhoneItemCodeArray[5]}, Description: {PhoneDescriptionArray[5]}, Price: ${PhonePriceArray[5]}')
        PhoneChoice = int(input('Please select a phone from the list, 1 to 6:   '))

        if PhoneChoice == 1:
            TotalPrice = TotalPrice + PhonePriceArray[0]
        elif PhoneChoice == 2:
            TotalPrice = TotalPrice + PhonePriceArray[1]
        elif PhoneChoice == 3:
            TotalPrice = TotalPrice + PhonePriceArray[2]
        elif PhoneChoice == 4:
            TotalPrice = TotalPrice + PhonePriceArray[3]
        elif PhoneChoice == 5:
            TotalPrice = TotalPrice + PhonePriceArray[4]
        elif PhoneChoice == 6:
            TotalPrice = TotalPrice + PhonePriceArray[5]
        else:
            Counter = 1
        ItemListArray.append(PhoneDescriptionArray[PhoneChoice - 1])
        print('Which SIM card would you like to purchase alongside the phone?')
        print(f'SIM Card 1: Code: {SIMCardItemCodeArray[0]}, Description: {SIMCardDescriptionArray[0]}, Price: ${SIMCardPriceArray[0]}')
        print(f'SIM Card 2: Code: {SIMCardItemCodeArray[1]}, Description: {SIMCardDescriptionArray[1]}, Price: ${SIMCardPriceArray[1]}')
        SIMCardChoice = int(input('Choose either 1 or 2 for the SIM you would like to choose: '))
        if SIMCardChoice == 1:
            TotalPrice = TotalPrice + SIMCardPriceArray[0]
        elif SIMCardChoice == 2:
            TotalPrice = TotalPrice + SIMCardPriceArray[1]
        else:
            Counter = 1
        ItemListArray.append(SIMCardDescriptionArray[SIMCardChoice - 1])
    elif Choice == 2:
        print(f'1. Tablet Code: {TabletItemCodeArray[0]}, Description: {TabletDescriptionArray[0]}, Price: ${TabletPriceArray[0]}')
        print(f'2. Tablet Code: {TabletItemCodeArray[1]}, Description: {TabletDescriptionArray[1]}, Price: ${TabletPriceArray[1]}')
        print(f'3. Tablet Code: {TabletItemCodeArray[2]}, Description: {TabletDescriptionArray[2]}, Price: ${TabletPriceArray[2]}')
        print(f'4. Tablet Code: {TabletItemCodeArray[3]}, Description: {TabletDescriptionArray[3]}, Price: ${TabletPriceArray[3]}')
        TabletChoice = int(input('Please select a tablet from the list, 1 to 4:    '))
        if TabletChoice == 1:
            TotalPrice = TotalPrice + TabletPriceArray[0]
        elif TabletChoice == 2:
            TotalPrice = TotalPrice + TabletPriceArray[1]
        elif TabletChoice == 3:
            TotalPrice = TotalPrice + TabletPriceArray[2]
        elif TabletChoice == 4:
            TotalPrice = TotalPrice + TabletPriceArray[3]
        else:
            Counter = 1
        ItemListArray.append(TabletDescriptionArray[TabletChoice - 1])
    print('Which case would you like to purchase?')
    print(f'1. Case Code: {CaseItemCodeArray[0]}, Description: {CaseDescriptionArray[0]}, Price: ${CasePriceArray[0]}')
    print(f'2. Case Code: {CaseItemCodeArray[1]}, Description: {CaseDescriptionArray[1]}, Price: ${CasePriceArray[1]}')
    CaseChoice = int(input(f'Type 1 for a {CaseDescriptionArray[0]} case, or type 2 for a {CaseDescriptionArray[1]} case:  '))

    if CaseChoice == 1:
        TotalPrice = TotalPrice + CasePriceArray[0]
    elif CaseChoice == 2:
        TotalPrice = TotalPrice + CasePriceArray[1]
    else:
        Counter = 1
    ItemListArray.append(CaseDescriptionArray[CaseChoice - 1])
    print('Which charger(s) would you like to purchase?')
    print(f'1. Charger Code: {ChargerItemCodeArray[0]}, Description:{ChargerDescriptionArray[0]}, Price: ${ChargerPriceArray[0]}')
    print(f'2. Charger Code: {ChargerItemCodeArray[1]}, Description:{ChargerDescriptionArray[1]}, Price: ${ChargerPriceArray[1]}')
    print(f'3. For both chargers')
    print(f'4. For no charger')
    ChargerChoice = int(input('Choose an option from the list above, between 1 and 4:  '))
    if ChargerChoice == 1:
        TotalPrice = TotalPrice + ChargerPriceArray[0]
        ItemListArray.append(ChargerDescriptionArray[0])
    elif ChargerChoice == 2:
        TotalPrice = TotalPrice + ChargerPriceArray[1]
        ItemListArray.append(ChargerDescriptionArray[1])
    elif ChargerChoice == 3:
        TotalPrice = TotalPrice + ChargerPriceArray[0] + ChargerPriceArray[1]
        ItemListArray.append(ChargerDescriptionArray[0]) and ItemListArray.append(ChargerDescriptionArray[1])
    else:
        Counter = 1
    print(f"Your cart's total is ${TotalPrice}")
    print(f'The breakdown of your chosen items are: {ItemListArray}')
    Counter = 1


