#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu


def computeFare(zone, ticketType):
     """
     Takes as two parameters: the zone and the ticket type.
     Returns the Copenhagen Transit fare, as follows:
     If the zone is 2 or smaller and the ticket type is "adult", the fare is 23.
     If the zone is 2 or smaller and the ticket type is "child", the fare is 11.5.
     If the zone is 3 and the ticket type is "adult", the fare is 34.5.
     If the zone is 3 or 4 and the ticket type is "child", the fare is 23.
     If the zone is 4 and the ticket type is "adult", the fare is 46.
     If the zone is greater than 4, return a negative number (since your calculator does not handle inputs that high).
     """

     fare = 0
     if zone <= 2:

        if ticketType== "adult":

            fare = 23

        else:

            fare = 11.5

     elif zone == 3:

        if ticketType== "adult":

            fare = 34.5

        else:

            fare = 23

     elif zone == 4:

        if ticketType== "adult":

            fare = 46

        else:

            fare = 23

     else:

        fare = -1

     return(fare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (adult/child): ').lower()
     fare = computeFare(z,t)
     print('The fare is', fare)

#Allow script to be run directly:
if name == "main":
     main()