def fuel_guage():
    while True:
        try: 
            digit = input('Fraction: ').split('/')
            x = int(digit[0])
            y = int(digit[-1])h
            
            if x == y:
                return 'F'
    
            elif y > x and x == 0:
                return 'E'
                
            elif y > x:
                fraction = x/y
                percentage = fraction * 100
                percentage = f'{percentage:.0f}'
                percentage_str = str(percentage) + '%'
                return percentage_str


        except ValueError:
            continue

        except ZeroDivisionError:
            continue

            
fuel_guage()