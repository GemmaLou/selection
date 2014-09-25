#Gemma Buckle 25/09/2014
#Asks user to input number between 1 and 20, tells them if it's in range.

def main():
    user_number=int(input("Please enter a number between 1 and 20: "))
    if user_number>=1 and user_number<=20:
        print("This is within the range!")
    elif user_number>20:
        print("This is too high.")
    elif user_number<1:
        print("This is too low.")
        
