number=[]
while True :
    score =input ("Enter a score or'Q' to exit: ")
    if score =="Q" or score == "q":
        break
    try:
        numbers.append(int(number))
    except ValueError:
        print("Only number is allowed!\n")
        if len (number):
            numbers= numbers[::1]
            print("\n Intergers in reversed oder:",end="")
        for num in numbers:
            print (num,end=" ")
        else:
            print("No intergers.")