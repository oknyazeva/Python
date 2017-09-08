string = "Hello, %s"
name = "User"
print string % name

string2 = "Hello, {}"
userName = raw_input("Enter User Name: ")
print string2.format(userName)
