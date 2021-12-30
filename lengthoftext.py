while True:
    text = input("Enter your text: \n ")

    if len(text)<10:
        print(" The text you put has less than 10 \n\n")
    elif len(text)==10:
        print(" Yes the text is equal  to 10 \n\n")
    else:
        print(" The text you entered is more than 10 \n\n")
