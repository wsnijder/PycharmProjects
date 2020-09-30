arrival = int(input("On what day do you arrive?"))
staying = int(input("What is the length of your stay?"))

dag = (arrival+staying)%7

if dag == 0:
    print("Sunday")
if dag == 1:
    print("Monday")
if dag == 2:
    print("Tuesday")
if dag == 3:
    print("Wednesday")
if dag == 4:
    print("Thursday")
if dag == 5:
    print("Friday")
if dag == 6:
    print("Saturday")