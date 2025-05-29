def main():
    plate = input('Plate: ') 
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')
        
        
def is_valid(s):
    for info in s:
        if info[0].isalpha() and info[1].isalpha():
            if len(s) <= 6:
                
            
        
    
    
    
    
    
main()