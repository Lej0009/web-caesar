def alphabet_position(letter):
    '''receive a letter and return the 0-based numerical position w/in the alphabet'''
    
    #alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    position = 0                           #initialize the position
    
    if letter.isalpha():                   #check if in alphabet
        position = alphabet.index(letter)  #if char is in the alphabet, get the position
        
    return position                        #return the position

def rotate_character(char, rot): 
    '''receives a character char and an integer rot. Returns the result of rotating 
    char by rot number of places to the right.'''
    
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    position = alphabet_position(char)     #set position equal to current position, getting it from alphabet_position function
    new_position = (position + rot) % 52   #set new position equal to the (old position + rotation) % total char in alphabet
                                           #so it will loop through the alphabet again once it hits Z
        
    if char.isalpha():                     #check if in alphabet
        new_char = alphabet[new_position]  #get letter from new position, set as new_char
    else:
        new_char = char                    #if not in alphabet, set new_char as original char
        
    return new_char                        #return the new character