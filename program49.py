#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu



n = float(input('Enter item price: '))
m = 0
total = 0

while n >= 0 :
    m = m + 1
    total = n + total 
    
    print('enter a dif price')
    n = float(input('Enter item price: '))
    
print('The average price of an item is: ', total/m)

    