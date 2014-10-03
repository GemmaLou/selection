#Gemma Buckle
#03/10/2014
#selection dev 4 grade check

mark = int(input("Please enter your exam mark to receive your grade: "))

if 0<=mark<=40:
    print("Your grade is U.")
elif 41<=mark<=50:
    print("Your grade is E.")
elif 51<=mark<=60:
    print("Your grade is D.")
elif 61<=mark<=70:
    print("Your grade is C.")
elif 71<=mark<=80:
    print("Your grade is B.")
elif 81<=mark<=100:
    print("Your grade is A!")
else:
    print("The mark you have entered is unacceptable. Please enter an integer between 0 and 100.")
    
