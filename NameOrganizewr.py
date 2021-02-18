#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu



mynames = input('Enter Names: ' )

namelist = mynames.split(' - ')



for aname in namelist:
    name = aname.split(' ')

    print(name[1] + ' ' + name[0][0] + '.' )