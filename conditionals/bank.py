def savings_bank():
    receptionist_reply = input().lower().strip().split(',')
    print(receptionist_reply)
    
    if receptionist_reply[0] == 'hello':
        return '$0'
    
    elif receptionist_reply[0][0] == 'h':
        return '$20'
    
    else:
        return '$100'

    
savings_bank()