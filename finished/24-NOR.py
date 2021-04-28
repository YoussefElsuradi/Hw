#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu


in1, in2 = input('True or False: '), input('True or False: ')

def NOR(in1, in2):
    if(in1 == False) and (in2 == False):
        return True
    elif(in1 == False) and (in2 == True):
        return False
    elif(in1 == True) and (in2 == False):
        return False
    elif(in1 == True) and (in2 == True):
        return False
 
out = ((in1 or in2) and (in1 or in2))
#print(NOR(in1,in2))