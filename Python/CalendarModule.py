import calendar

month, day, year = input().split()

dayOfWeek = calendar.weekday(int(year), int(month), int(day))

match(dayOfWeek):
    case 0:
        print('MONDAY')
    case 1:
        print('TUESDAY')
    case 2:
        print('WEDNESDAY')
    case 3:
        print('THURSDAY')
    case 4:
        print('FRIDAY')
    case 5:
        print('SATURDAY')
    case 6:
        print('SUNDAY')
