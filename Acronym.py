#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu
#prints acronym of user input backwords


def main():
    text = input('Enter Message: ') #user input
    text_split = text.split()  #split phrase into individual strings
    
    text_upper = text.upper()
    print(text_upper)    
    acronym = ""
    
    for i in text_split:
        acronym = acronym + i[0].upper()
    print('Acronym: ', acronym[::-1])
    

main()