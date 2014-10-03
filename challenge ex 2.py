#Gemma Buckle
#03/10/2014
#selection challenge 2

day_num = int(input("Please enter the day as a number, as dd: "))
if day_num==1 or day_num==21 or day_num==31:
    day_word=("{0}st".format(day_num))
elif day_num==2 or day_num==22:
    day_word=("{0}nd".format(day_num))
elif day_num==3 or day_num==23:
    day_word=("{0}rd".format(day_num))
elif 0>=day_num>=32:
    print("The day you have entered is unnaceptable. Please enter an integer between 1 and 31.")
else:
    day_word=("{0}th".format(day_num))

month_num=int(input("Please enter the month as a number, as mm: "))
if month_num == 1:
    month_word=("January")
elif month_num == 2:
    month_word=("February")
elif month_num == 3:
    month_word=("March")
elif month_num == 4:
    month_word=("April")
elif month_num == 5:
    month_word=("May")
elif month_num == 6:
    month_word=("June")
elif month_num == 7:
    month_word=("July")
elif month_num == 8:
    month_word=("August")
elif month_num == 9:
   month_word=("September")
elif month_num == 10:
    month_word=("October")
elif month_num == 11:
    month_word=("November")
elif month_num == 12:
    month_word=("December")
else:
    print("The month you have entered is unacceptable. Please enter an integer between 1 and 12.")

year_num=int(input("Please enter the year as a number, as yy: "))
if 1<=year_num<=9:
    year_full=("200{0}".format(year_num))
elif 10<=year_num<=99:
    year_full=("20{0}".format(year_num))
else:
    print("Year entered is unacceptable. Please enter a year as yy between 00 and 99.")

print("The full date is {0} {1} {2}!".format(day_word,month_word,year_full))
