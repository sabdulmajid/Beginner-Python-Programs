#BY AWAB AQIB
#https://www.youtube.com/channel/UC9S3DDVJNbN1ILrV0HTUn6w
#If you do not watch the video, you will not understand the pseudocode or the Python code!

##################TASK # 1

phoneCodes=   ["BPCM",    "BPSH",        "RPSS",                                         "RPLL"]
phoneDesc=  ["Compact", "Clam Shell",  "RoboPhone – 5-inch screen and 64GB memory",    "RoboPhone – 6-inch screen and 256GB memory"]
phonePrice= [29.99,        49.99,          199.99,                                         499.99]

tabletCodes=  ["RTMS",                                      "RTLM"]
tabletDesc= ["RoboTab – 8-inch screen and 64GB memory",     "RoboTab – 8-inch screen and 64GB memory"]
tabletPrice= [149.99,       299.99]

simCodes= ["SMNO",       "SMPG"]
simDesc=  ["Sim Free", "Pay As You Go"]
simPrice=  [0.00,        9.99]

caseCodes= ["CSST",     "CSLX"]
caseDesc=  ["Standard",  "Luxury"]
casePrice=  [0.00,          50.00]

chargerCodes= ["CGCR",  "CGHM"]
chargerDesc=  ["Car",   "Home"]
chargerPrice= [19.99,   15.99]

totalPrice=0.0
currentProduct=""
bill=[]
outputList=[]


while(True):
    ##############################################Phone input
    choice = int(input("What do you want to buy? Press 1. Phone or 2. for Tablet: "))
    if(choice==1):
        print("Press 1. for", phoneCodes[0],phoneDesc[0],"$",phonePrice[0])
        print("Press 2. for", phoneCodes[1],phoneDesc[1],"$",phonePrice[1])
        print("Press 3. for", phoneCodes[2],phoneDesc[2],"$",phonePrice[2])
        print("Press 4. for", phoneCodes[3],phoneDesc[3],"$",phonePrice[3])

        phoneType= int(input("What type of phone you want to buy? Enter that number: "))
        if(phoneType== 1 or phoneType== 2 or phoneType== 3 or phoneType== 4):
            itemCode = phoneCodes[phoneType-1]
            itemDesc = phoneDesc[phoneType-1]
            itemPrice = phonePrice[phoneType-1]

            outputList.append(itemCode)
            outputList.append(itemDesc)

            bill.append(float(itemPrice))


            print("\nPress 1. for",simCodes[0],simDesc[0],"$",simPrice[0])
            print("Press 2. for",simCodes[1],simDesc[1],"$",simPrice[1])
            simType= int(input("Which SIM do you want to buy?"))
            if(simType== 1 or simType==2):

                sCode = simCodes[simType-1]
                sDesc = simDesc[simType-1]
                sPrice = simPrice[simType-1]

                outputList.append(sCode)
                outputList.append(sDesc)

                bill.append(float(sPrice))



            else:
                print("\nPlease press 1. or 2. to select a proper SIM type")
                continue

        else:
            print("\nPlease press an option from 1,2,3,4 for your choice of Phone!")
            continue


    ##############################################Tablet input
    elif(choice==2):
        print("\nPress 1. for", tabletCodes[0],tabletDesc[0],"$",tabletPrice[0])
        print("Press 2. for", tabletCodes[1],tabletDesc[1],"$",tabletPrice[1])

        tabType = int(input("What type of tablet you want to buy? Enter that number: "))
        if(tabType == 1 or tabType == 2):
            itemCode = tabletCodes[tabType-1]
            itemDesc = tabletDesc[tabType-1]
            itemPrice = tabletPrice[tabType-1]


            outputList.append(itemCode)
            outputList.append(itemDesc)

            bill.append(float(itemPrice))

        else:
            print("\nPlease press 1 or 2 for your choice of Tablet!")
            continue

    else:
        print("\nPlease enter 1. for Phone and 2. for Tablet!")
        continue

    ##############################################Case input

    print("\nPress 1. for", caseCodes[0],caseDesc[0],"$",casePrice[0])
    print("Press 2. for", caseCodes[1],caseDesc[1],"$",casePrice[1])
    caseType= int(input("Which Case do you want to buy?"))

    if(caseType== 1 or caseType==2):

        cCode = caseCodes[caseType-1]
        cDesc = caseDesc[caseType-1]
        cPrice = casePrice[caseType-1]

        outputList.append(cCode)
        outputList.append(cDesc)

        bill.append(float(cPrice))


    else:
        print("\nPlease press 1. or 2. to select a proper SIM type")
        continue


    ##############################################Charger input

    print("\nPress 1. for NO charger.")
    print("Press 2. for EITHER  Car-$19.99 / Home charger-15.99")
    print("Press 3. for BOTH Car-$19.99 / Home charger-15.99")

    chargerType= int(input("Which option for Charger do you want to buy?"))

    if(chargerType==2):
        print("Press 1. for Car Charger-$19.99")
        print("Press 2. for Home Charger-$15.99")

        chargerTypeNew = int(input("Which option for Charger do you want to buy?"))
        if(chargerTypeNew==1 or chargerTypeNew==2):
            cgCode = chargerCodes[chargerType-1]
            cgDesc = chargerDesc[chargerType-1]
            cgPrice = chargerPrice[chargerType-1]

            outputList.append(cgCode)
            outputList.append(cgDesc)

            bill.append(float(cgPrice))

        else:
            print("Please press 1. or 2. for buying either of the chargers!")
            continue

    elif(chargerType==3):
        print("You have chosen to buy both home and car chargers!")
        outputList.append(chargerCodes[0])
        outputList.append(chargerDesc[0])

        outputList.append(chargerCodes[1])
        outputList.append(chargerDesc[1])

        bill.append(float(chargerPrice[0]))
        bill.append(float(chargerPrice[1]))




    elif(chargerType==1):
        print("You have chosen to buy no charger!")


    else:
        print("\nPlease press 1. or 2. to select a proper Charger type")
        continue

    #################################################Additional Phone
    print("\nDo you want to buy another Mobile? Press 1. for Yes. Press 2. for No.")
    additionalPhone = int(input("Kindly enter your choice for another phone: "))

    if(additionalPhone == 1):
        print("\nList of items purchased : ")
        print(outputList)

        print("\nBreakdown bill of your purchases: ")
        for x in bill:
            print(x)

        print("\nTotal bill so far: ")
        print(sum(bill))

        continue


    ##############################################
    elif(additionalPhone ==2):

        print("\nList of items purchased : ")
        print(outputList)

        print("\nBreakdown bill of your purchases: ")
        for x in bill:
            print(x)

        print("\nTotal bill: ")
        print(sum(bill))

        break





