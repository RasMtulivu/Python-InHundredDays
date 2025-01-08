year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0 == False:
        print(f"{year} is a leap year")
    elif (year % 100) == (year % 400):
        print(f"{year} is a leap year")
else:
     print(f"{year} is not a leap year")