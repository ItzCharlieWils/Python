#logical operators = evaluate multiple conditions (or, and, not)
#           or = at least one condition must be true
#           and = both conditions must be true
#           not = invert the conditions(not False, not True)


#Or operator
#temp = 20
#is_raining = False

#if temp >35 or temp < 0 or is_raining:
#    print("You can't do outdoor events")
#else:
#    print("You can do outdoor activities and events ")


#and, not operator

temp = 30
is_sunny = False

if temp>=28 and is_sunny:
    print("It's hot and sunny outside")
elif temp <=0 and is_sunny:
    print("it is cold and sunny outside")
elif temp <=0 and not is_sunny:
    print("it is cold and not sunny outside")
elif 28>temp>0 and not is_sunny:
    print("it is warm and not sunny outside")
elif 0<temp<28 and is_sunny :
    print("it is warm and sunny outside")
else :
    print("Something terrible is happening outside!!")

    