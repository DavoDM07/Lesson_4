#The program prompts the user their birth year. Assuming a person’s age
#is a non-negative integer not exceeding 120, output the user’s age or the
#words “Incorrect Year”. The sample outputs assume it’s currently the year
#2016. If you are writing this program during any other year, the correct
#answers may differ. Store the value of the current year in a variable.


now = 2016
my_year = 1999
age = now - my_year
if my_year > now:
    print("Incorrect Year")
else:
    print(age)