a = 4

print("I have a number in my mind. can you guess?")

mynum = int(input("Enter the  guess number "))

if a== mynum:
    print(" yes i guess the right number") 

elif mynum > a:
    print("The number is greater that you entered")

else:
    print("the number is smaller that you entered")
