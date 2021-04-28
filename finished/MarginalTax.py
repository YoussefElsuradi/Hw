#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu


mess = int(input('Enter your Income: '))

if mess <= 0 :
    print('Error')
elif mess <= 9700 :
    print('marginal tax rate: 10%')
    
elif  mess <= 39475:
    print('marginal tax rate: 12%')
    
elif mess <= 84200 :
    print('marginal tax rate: 22%')
    
elif mess <= 160725 :
    print('marginal tax rate: 24%')
    
elif mess <= 204100 :
    print('marginal tax rate: 32%')
    
elif mess <= 510300 :
    print('marginal tax rate: 35%')
    
elif mess >= 510301 :
    print('marginal tax rate: 37%')
    