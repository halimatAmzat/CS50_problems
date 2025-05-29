def main():
    current_time = input('What is the time? ')
    the_time = convert(current_time)
    the_time = float(the_time)

    if 7.00 <= the_time <= 8.00:
        return 'Breakfast'
    elif 12.00 <= the_time <= 13.00:
        return 'Lunch'
    elif 19.00 <= the_time <= 20.00:
        return 'Dinner'
    
    
def convert(time):
    hours, minutes = time.split(':')
    minutes = int(minutes) / 60
    the_hours = int(hours) + minutes
    the_hours_dp = f'{the_hours:.2f}'
    return the_hours_dp
        
if "_name_" == "_main_":
    main()



main()

