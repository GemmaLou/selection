#Gemma Buckle 25/09/2014
#Evaluates if the user can vote and tells them when they can retire.

user_age=int(input("Please enter your age: "))
if user_age>=18:
    print("You are old enough to vote!")
else:
    print("Your are not old enough to vote.")
retirement=65-user_age
print("You have {0} years until you can retire :]".format(retirement))
