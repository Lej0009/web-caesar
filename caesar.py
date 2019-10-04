from helpers import alphabet_position, rotate_character     #import helper functions

def rotate_string(text, rot):
    """Function to encrypt the message."""
    
    encrypt_msg = ''                         #initialize new string 'encrypt_msg'
    for letter in text:                      #iterate through each char in string 'text' which is user input message
        new_letter = rotate_character(letter, rot)   #set the new_letter that will replace the current, using rotate_character
        if letter == ' ':                    #checking if letter is a <space>
            encrypt_msg += ' '               #add <space> to encrypted message
        else:
            encrypt_msg += new_letter        #if char is not alphanumeric, just return the original char in encrypted message
            
    return encrypt_msg                       #return the new encrypted message

def main():
    from sys import argv, exit               #import what user input (rotation amount) on cmd prompt and import exit from sys
        
    if argv[1].isdigit() == True:            #if user input (rot amt) is a digit, return True
        text = input("Input message:")       #get message to encrypt from the user
        rot = int(argv[1])                   #set rot to the rotation amount user input on cmd prompt
        print(rotate_string(text, rot))            #call encrypt function and print result
    else:                                    #if user did not input an integer for rotation amt on cmd line, return error message
        print("""usage: python vigenere.py rotation amount
Arguments:
-rotation amount : This is how many positions to the right your encryption key will be. Should only contain an integer-- no alphabetic or special characters.""")
        exit()
        
    
if __name__ == "__main__":
    main()