a = 13

print(" I CAN GUESS THE NUMBER THAT IS ON YOUR MIND. DO U WANT TO TRY?")

while True:
    usernum = int(input("Enter your guess number: "))

    if usernum == a:
        print(" yes i guess the number")

    elif usernum>a:
        print(" The number you choose is greater")

    elif usernum<a:
        print(" the number you choose is lesser ")

    else:
        print(" the number you choose is invalid", usernum.get(a))