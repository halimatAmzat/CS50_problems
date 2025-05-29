def convert():
    text = input()
    #replace the emocons with emojis
    text = text.replace(':)', '🙂') 
    text = text.replace(':(', '🙁')
    return text
    
    
convert()   
