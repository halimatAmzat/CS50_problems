def coin():
    global amount_due
    count = 0
    amount_due = 50
    print('Amount Due: ', amount_due)

#     change_owed = 50
    while True:

        if count < 50:
            
            the_coin = int(input('Insert coin: '))
#             print(type(the_coin))
            if the_coin in [50, 25, 10]:
                count += the_coin
               
                amount_due = amount_due - the_coin
                print(amount_due)
                print('count: ', count)
               
#                 change_owed -= int(the_coin)

                
            else:
                continue
                
#         print('change owed: ', change_owed)
                
                
       
coin()
    
    