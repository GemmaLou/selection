#Gemma Buckle
#10/10/2014
#Mr/Ms [name]

first_name=input("Please enter your first name: ")
last_name=input("Please enter your last name: ")
gender=input("Please enter your gender(m/f): ")
if gender=="m":
    print("Mr {0} {1}.".format(first_name, last_name))
elif gender=="f":
    print("Ms {0} {1}.".format(first_name, last_name))
else:
    print("Please enter an appropriate gender.")
    
