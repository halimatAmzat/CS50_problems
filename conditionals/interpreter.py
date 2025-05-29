def interpreter():
    calculator = input()
    x, y, z = calculator.split(' ')
    x = int(x)
    y = y
    z = int(z)
    if y == '+':
        return float((f'{x + z:.1f}'))
    elif y == '-':
        return float((f'{x - z:.1f}'))
    elif y == '*':
        return float((f'{x * z:.1f}'))
    elif y == '/':
        return float((f'{x / z:.1f}'))
    

    

    
    
interpreter()