#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu


    
    
from string import ascii_lowercase as ALPHABET

def shift(message, offset):
    
    trans = str.maketrans(ALPHABET, ALPHABET[offset:] + ALPHABET[:offset])
    
    return message.lower().translate(trans)  #keeps everything lower case cuz we the cipher can't handle upper case letters yet

print(shift(input("Input message you would like encrypted:\n"), 13).upper())