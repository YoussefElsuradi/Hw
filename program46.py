#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu

NumberDay = int(input("enter the number of the day: "))

while (NumberDay<1 or NumberDay>7):
    NumberDay = int(input("Not valid day number. Enter a number between 1 and 7: "));
arr = ["","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print("The day is",arr[NumberDay])
    
