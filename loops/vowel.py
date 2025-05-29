def non_vowel():
    
    new_word = ''
    word = input('Input: ')
    for letter in word:

        if letter in 'aeiou':
            continue
        else:
            new_word += letter
    return f'Output: {new_word}'
            

            
non_vowel()