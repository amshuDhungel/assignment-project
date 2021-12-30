a = 4

print("I have a number in my mind. can you guess?")

while True:
    mynum = int(input("Enter the  guess number "))


    if a== mynum:
        print(" yes i guess the right number", end ="\n\n") 

    elif mynum > a:
        print("The number is greater that you entered.next" ,end = "\n\n")

    else:
        print("the number is smaller that you entered. next? ",end = "\n\n")
