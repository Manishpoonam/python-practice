# Match(its like a switch)

day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _: #For Default Value
        print("Invalid Entry")

#Combine Value------------------
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is week day")
    case 6 | 7:
        print("Today is week end")

# If Statements as Guards-----------
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")




