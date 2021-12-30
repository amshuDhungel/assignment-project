mydict = {"mirga": "deer",
"sutnu":"sleep",
"manche": "man",
"cartoon":"anime"

}
print("the Options are", mydict.keys())
a = input("Enter the word: " "\n")
print("The meaning of a word is: ",mydict.get(a))

