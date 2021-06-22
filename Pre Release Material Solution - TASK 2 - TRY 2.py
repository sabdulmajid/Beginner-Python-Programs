# Pre Release Material Solution.py
PhoneDescriptionArray = ['Compact - Phone',
                         'Clam Shell - Phone',
                         'RoboPhone - 5-inch screen and 64GB memory - Phone',
                         'RoboPhone - 6-inch screen and 256GB memory - Phone',
                         'Y-Phone Standard - 6-inch screen and 64GB memory - Phone',
                         'Y-Phone Standard - 6-inch screen and 256GB memory - Phone']
PhoneItemCodeArray = ['BPCM', 'BPSH', 'RPSS', 'RPLL', 'YPLS', 'YPLL']
PhonePriceArray = [29.99, 49.99, 199.99, 499.99, 549.99, 649.99]


TabletItemCodeArray = ['RTMS', 'RTLM', 'YTLM', 'YTLL']
TabletDescriptionArray = ['RoboTab - 8-inch screen and 64GB memory - Tablet',
                          'RoboTab - 10-inch screen and 128GB memory - Tablet',
                          'Y-Tab Standard - 10-inch screen and 128GB memory - Tablet',
                          'Y-Tab Deluxe - 10-inch screen and 256GB memory - Tablet']
TabletPriceArray = [149.99, 299.99, 499.99, 599.99]


SIMCardItemCodeArray = ['SMNO', 'SMPG']
SIMCardDescriptionArray = ['SIM Free (no SIM card purchased) - SIM card',
                           'Pay As You Go (SIM card purchased) - SIM card']
SIMCardPriceArray = [0.00, 9.99]


CaseItemCodeArray = ['CSST', 'CSLX']
CaseDescriptionArray = ['Standard - Case',
                        'Luxury - Case']
CasePriceArray = [0.00, 50.00]


ChargerItemCodeArray = ['CGCR', 'CGHM']
ChargerDescriptionArray = ['Car - Charger',
                           'House  - Charger']
ChargerPriceArray = [19.99, 15.99]

TotalPrice = 0.00
ItemListArray = []
OutputList = []

DiscountedPrice = []
Discount = 0.00
Length = 0
IndividualBill = []
index = 0
TotalDiscount = 0.00

while True:

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

        if PhoneChoice == 1 or PhoneChoice == 2 or PhoneChoice == 3 or PhoneChoice == 4 or PhoneChoice == 5 or PhoneChoice == 6:
            ItemCode = PhoneItemCodeArray[PhoneChoice - 1]
            ItemDescription = PhoneDescriptionArray[PhoneChoice - 1]
            ItemPrice = PhonePriceArray[PhoneChoice - 1]

            OutputList.append(ItemCode)
            OutputList.append(ItemDescription)

            ItemListArray.append(float(ItemPrice))

            print(f'SIM Card 1: Code: {SIMCardItemCodeArray[0]}, Description: {SIMCardDescriptionArray[0]}, Price: ${SIMCardPriceArray[0]}')
            print(f'SIM Card 2: Code: {SIMCardItemCodeArray[1]}, Description: {SIMCardDescriptionArray[1]}, Price: ${SIMCardPriceArray[1]}')

            SIMCardChoice = int(input('Choose either 1 or 2 for the SIM you would like to choose: '))

            if SIMCardChoice == 1 or SIMCardChoice == 2:

                SIMCode = SIMCardItemCodeArray[SIMCardChoice - 1]
                SIMDescription = SIMCardDescriptionArray[SIMCardChoice - 1]
                SIMPrice = SIMCardPriceArray[SIMCardChoice - 1]

                OutputList.append(SIMCode)
                OutputList.append(SIMDescription)

                ItemListArray.append(float(SIMPrice))

            else:
                print("Please press 1 or 2 to select a proper SIM type")
                continue

        else:
            print("Please press an option from 1, 2, 3, 4, 5 or 6 for your choice of phone!")
            continue

    elif Choice == 2:
        print(f'1. Tablet Code: {TabletItemCodeArray[0]}, Description: {TabletDescriptionArray[0]}, Price: ${TabletPriceArray[0]}')
        print(f'2. Tablet Code: {TabletItemCodeArray[1]}, Description: {TabletDescriptionArray[1]}, Price: ${TabletPriceArray[1]}')
        print(f'3. Tablet Code: {TabletItemCodeArray[2]}, Description: {TabletDescriptionArray[2]}, Price: ${TabletPriceArray[2]}')
        print(f'4. Tablet Code: {TabletItemCodeArray[3]}, Description: {TabletDescriptionArray[3]}, Price: ${TabletPriceArray[3]}')

        TabletChoice = int(input('Please select a tablet from the list, 1 to 4:    '))

        if TabletChoice == 1 or TabletChoice == 2 or TabletChoice == 3 or TabletChoice == 4:
            ItemCode = TabletItemCodeArray[TabletChoice - 1]
            ItemDescription = TabletDescriptionArray[TabletChoice - 1]
            ItemPrice = TabletPriceArray[TabletChoice - 1]

            OutputList.append(ItemCode)
            OutputList.append(ItemDescription)

            ItemListArray.append(float(ItemPrice))

        else:
            print('Invalid number. Please choose from the list 1 - 4:  ')
            continue

    else:
        print('Invalid number. Please enter 1 for phone or 2 for tablet:  ')


    print('Which case would you like to purchase?')
    print(f'1. Case Code: {CaseItemCodeArray[0]}, Description: {CaseDescriptionArray[0]}, Price: ${CasePriceArray[0]}')
    print(f'2. Case Code: {CaseItemCodeArray[1]}, Description: {CaseDescriptionArray[1]}, Price: ${CasePriceArray[1]}')
    CaseChoice = int(input(f'Type 1 for a {CaseDescriptionArray[0]} case, or type 2 for a {CaseDescriptionArray[1]} case:  '))

    if CaseChoice == 1 or CaseChoice == 2:
        CaseCode = CaseItemCodeArray[CaseChoice - 1]
        CaseDescription = CaseDescriptionArray[CaseChoice - 1]
        CasePrice = CasePriceArray[CaseChoice - 1]

        OutputList.append(CaseCode)
        OutputList.append(CaseDescription)

        ItemListArray.append(float(CasePrice))
    else:
        print('Wrong input, please enter a SIM choice: ')
        continue

    print('Which charger(s) would you like to purchase?')
    print('1. No charger opted.')
    print(f'2. To choose between either {ChargerDescriptionArray[0]} or {ChargerDescriptionArray[1]} ')
    print('3. To choose both the chargers.  ')

    ChargerChoice = int(input('Which option would you like to select?'))

    if ChargerChoice == 1:
        print('You have chosen to buy no charger!')

    elif ChargerChoice == 2:
        print(f'Press 1 for {ChargerDescriptionArray[0]}'
              f'Press 2 for {ChargerDescriptionArray[1]}')

        SecondChargerChoice = int(input(f'Which option would you like, 1 for {ChargerDescriptionArray[0]} or 2 for {ChargerDescriptionArray[1]}?'))
        if SecondChargerChoice == 1 or SecondChargerChoice == 2:
            ChargerCode = ChargerItemCodeArray[ChargerChoice - 1]
            ChargerDescription = ChargerDescriptionArray[ChargerChoice - 1]
            ChargerPrice = ChargerPriceArray[ChargerChoice - 1]

            OutputList.append(ChargerCode)
            OutputList.append(ChargerDescription)

            ItemListArray.append(float(ChargerPrice))

        else:
            print("Invalid data. Please input the correct data:  ")
            continue

    elif ChargerChoice == 3:
        print("You have chosen to buy both the Home and Car chargers.")
        OutputList.append(ChargerItemCodeArray[0])
        OutputList.append(ChargerDescriptionArray[0])

        OutputList.append(ChargerItemCodeArray[1])
        OutputList.append(ChargerDescriptionArray[1])

        ItemListArray.append(float(ChargerPriceArray[0]))
        ItemListArray.append(float(ChargerPriceArray[1]))

    else:
        print('Invalid data inputted. Please enter the correct data:  ')
        continue

    print('Do you want to buy another device? Press 1 for yes, or 2 for no:  ')
    AdditionalPhone = int(input("Enter your choice:  "))

    if AdditionalPhone == 1:
        print("\nList of items purchased: ")
        for y in OutputList:
            print(y)

        print("\nBreakdown bill of your purchases: ")
        for x in ItemListArray:
            print(x)

        Discount = sum(ItemListArray) * 0.1
        UpdatedPrice = sum(ItemListArray) - Discount
        TotalDiscount = TotalDiscount + Discount

        print(f'Discounted price with 10% off: ${UpdatedPrice}')
        print(f'Money saved so far: ${TotalDiscount}')

        IndividualBill.append(UpdatedPrice)

        print("\nTotal bill so far: ")
        print(sum(ItemListArray))

        continue

    elif AdditionalPhone == 2:

        print("\nList of items purchased: ")
        for y in OutputList:
            print(y)

        print("\nBreakdown bill of your purchases: ")
        for x in ItemListArray:
            print(f'${x}')

        print(f"\nTotal bill: ${sum(ItemListArray)}")

        break




