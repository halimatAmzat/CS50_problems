user = input('camelCase: ')
camel_case = ''
for letter in user:
    if letter.isupper():
        camel_case = camel_case+'_'+letter.lower()
        
    else:
        camel_case += letter
        
print(camel_case)
        
        