post = input(" Enter your post: ")
post.casefold()
if post.find("harry"):
    print("This post is about harry")
elif post.find("Harry"):
    print("The post is  talking about harry")
elif post.find("HARRY"):
    print(" This post is about harry")
else:
    print("This is not about harry")