#Gemma Buckle
#10/09/2014
#selection development water temp

temp=int(input("Please enter the temperature of the water in the container in degrees centigrade: "))
if temp>=100:
    print("This water is boiling.")
elif temp<=0:
    print("This water is frozen.")
else:
    print("This water is neither boiling nor frozen.")
    
