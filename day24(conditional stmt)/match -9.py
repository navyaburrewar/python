## match ##
## combine values

#Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
day =3
match day:
    case 1|2|3|4:
        print("holiday")
    case 5|6|7:
        print("not holiday")    

#Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:


month =6
day=6
match day:
    case 2|4|6 if month ==4:
        print("a weekday in april")
    case 2|3|6 if month==6:
        print("a weekday in june")    