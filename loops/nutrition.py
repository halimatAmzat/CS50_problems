def nutrition():
    consumer =input('Input the fruit you want to know its calories: ').title().strip()
    fruit_dict = {'Apple':130,
                  'Avocado California':50,
                  'Banana':110,
                  'Cantaloupe':50,
                  'Grapefruit':60,
                  'Grapes':90,
                  'Honeydew Melon':50,
                  'Kiwifruit':90,
                  'Lemon':15,
                  'Lime':20,
                  'Nectarine':60,
                  'Orange':80,
                  'Peach':60,
                 'Pear': 100,
                  'Pineapple':50,
                  'Plums':70,
                  'Strawberries':50,
                  'Sweet Cherries':100,
                  'Tangerine':50,
                  'Watermelon':80}
    for fruit in fruit_dict:
        if consumer == fruit:
            calories = fruit_dict[fruit]
            print(calories)
            return calories
       
            
nutrition()          
            