Phone_Item_code=['BPCM',
       'BPSH',
       'RPSS',
       'RPLL',
       'YPLS',
       'YPLL']
Phone_Description=['Compact',
                   'Clam shell',
                   'RoboPhone - 5-inch screen and 64GB memory',
                   'RoboPhone - 6-inch screen and 256GB memory',
                   'Y-Phone Standard - 6-inch screen and 64GB memory',
                   'Y-Phone Standard - 6-inch screen and 256GB memory' ]
Phone_Price=[29.99,
             49.99,
             199.99,
             499.99,
             549.99,
             649.99]

Tablet_item_code=['RTMS',
                  'RTLM',
                  'YTLM',
                  'YTLL']
Tablet_Description=['RoboTab - 8-inch screen and 64GB memory',
                    'RoboTab - 10-inch screen and 128GB memory',
                    'Y-Tab Standard - 10-inch screen and 128GB memory',
                    'Y-Tab Deluxe- 10-inch screen and 256GB memory']
Tablet_Price=[149.99,
              299.99,
              499.99,
              599.99]

SIM_card_item_code=['SMNO',
                   'SMPG']
SIM_card_Description=['SIM Free (no SIM card purchased)',
                     'Pay As You Go (SIM card purchased)']
SIM_card_Price=[0.00,
               9.99]

Case_item_code=['CSST',
                'CSLX']
Case_Description=['Standard',
                  'Luxury']
Case_Price=[0.00,
            50.00]

Charger_item_code=['CGCR',
                   'CGHM']
Charger_Description=['Car',
                     'House']
Charger_Price=[19.99,
               15.99]

Overall_price=0
i=0
Item_List=[]

while i==0:

  Choosing=int(input('For a Phone type 1 , For a Tablet type 2 '))

  if Choosing==1:
      print(f'Phone 1: Code:{Phone_Item_code[0]}, Description:{Phone_Description[0]}, Price: ${Phone_Price[0]}')
      print(f'Phone 2: Code:{Phone_Item_code[1]}, Description:{Phone_Description[1]}, Price: ${Phone_Price[1]}')
      print(f'Phone 3: Code:{Phone_Item_code[2]}, Description:{Phone_Description[2]}, Price: ${Phone_Price[2]}')
      print(f'Phone 4: Code:{Phone_Item_code[3]}, Description:{Phone_Description[3]}, Price: ${Phone_Price[3]}')
      print(f'Phone 5: Code:{Phone_Item_code[4]}, Description:{Phone_Description[4]}, Price: ${Phone_Price[4]}')
      print(f'Phone 6: Code:{Phone_Item_code[5]}, Description:{Phone_Description[5]}, Price: ${Phone_Price[5]}')
      Phone=int(input('Type a number between 1-6 to choose the Phone you want to buy '))

      if Phone==1:
          Overall_price= Overall_price+Phone_Price[0]
      elif Phone==2:
           Overall_price = Overall_price + Phone_Price[1]
      elif Phone==3:
            Overall_price = Overall_price + Phone_Price[2]
      elif Phone==4:
           Overall_price = Overall_price + Phone_Price[3]
      elif Phone==5:
           Overall_price = Overall_price + Phone_Price[4]
      elif Phone==6:
           Overall_price = Overall_price + Phone_Price[5]
      else:
        i=1
      Item_List.append(Phone_Description[Phone-1])
      print('What kind of SIM Card do you want?')
      print(f'SIM Card 1: Code:{SIM_card_item_code[0]}, Description:{SIM_card_Description[0]}, Price: ${SIM_card_Price[0]}')
      print(f'SIM Card 2: Code:{SIM_card_item_code[1]}, Description:{SIM_card_Description[1]}, Price: ${SIM_card_Price[1]}')
      SIM_card=int(input('Choose either 1 or 2 for the SIM you want: '))
      if SIM_card==2:
          Overall_price=Overall_price+SIM_card_Price[1]
      else:
          i=1
      Item_List.append(SIM_card_Description[SIM_card- 1])
  elif Choosing==2:
      print(f'Tablet 1: Code:{Tablet_item_code[0]}, Description:{Tablet_Description[0]}, Price: ${Tablet_Price[0]}')
      print(f'Tablet 2: Code:{Tablet_item_code[1]}, Description:{Tablet_Description[1]}, Price: ${Tablet_Price[1]}')
      print(f'Tablet 3: Code:{Tablet_item_code[2]}, Description:{Tablet_Description[2]}, Price: ${Tablet_Price[2]}')
      print(f'Tablet 4: Code:{Tablet_item_code[3]}, Description:{Tablet_Description[3]}, Price: ${Tablet_Price[3]}')
      Tablet=int(input('Type a number between 1-4 to choose the Tablet you want to buy: '))

      if Tablet==1:
          Overall_price=Overall_price+Tablet_Price[0]
      elif Tablet==2:
          Overall_price = Overall_price + Tablet_Price[1]
      elif Tablet==3:
          Overall_price = Overall_price + Tablet_Price[2]
      elif Tablet==4:
          Overall_price = Overall_price + Tablet_Price[3]
      else:
          i=1
      Item_List.append(Tablet_Description[Tablet-1])
  print('What case would you like to buy?')
  print(f'Case 1: Code:{Case_item_code[0]}, Description:{Case_Description[0]}, Price: ${Case_Price[0]}')
  print(f'Case 2: Code:{Case_item_code[1]}, Description:{Case_Description[1]}, Price: ${Case_Price[1]}')
  Case=int(input('What case do you want, 1 or 2? '))
  if Case==2:
      Overall_price=Overall_price+Case_Price[0]
  else:
      i=1
  Item_List.append(Case_Description[Case - 1])
  print('Which Charger(s) would you like to buy?')
  print(f'Charger 1: Code:{Charger_item_code[0]}, Description:{Charger_Description[0]}, Price: ${Charger_Price[0]}')
  print(f'Charger 2: Code:{Charger_item_code[1]}, Description:{Charger_Description[1]}, Price: ${Charger_Price[1]}')
  Charger=int(input('Type 1 for charger 1, 2 for charger 2, 3 for both chargers and 4 for neither: '))
  if Charger==1:
      Overall_price=Overall_price+Charger_Price[0]
      Item_List.append(Charger_Description[0])
  elif Charger==2:
      Overall_price=Overall_price+Charger_Price[1]
      Item_List.append(Charger_Description[1])
  elif Charger==3:
      Overall_price=Overall_price+Charger_Price[1]+Charger_Price[0]
      Item_List.append(Charger_Description[0])
      Item_List.append(Charger_Description[1])
  else:
      i=1

  print(f'Your items price is ${Overall_price}')
  print(f'The list of your chosen items is {Item_List}')
  i=1
