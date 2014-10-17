#Gemma Buckle
#10/10/2014
#Attendance check

attendance=int(input("Please enter your attendance as a percentage: "))
if 85<attendance<100:
    print("Your attendance is {0}%. Keep up the good attendance.".format(attendance))
elif 0<=attendance<=85:
    print("Your attendance is only {0}%. You must improve your attendance.".format(attendance))
else:
    print("{0}% is not an acceptable value.".format(attendance))
