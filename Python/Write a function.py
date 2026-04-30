def is_leap(year):
    leap = False
    if (year /4).is_integer() == True:
        leap = True
    if (year/100).is_integer() == True:
        leap = False
    if (year/400).is_integer() == True:
        leap = True
    return leap
            

year = int(input())
print(is_leap(year))
