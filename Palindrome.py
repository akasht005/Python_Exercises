
string = ["noon"]

x = list(filter(lambda a : a == a[::-1], string))

if x == string:
    print("noon is a palindrom")

else:
    print("Not a palindrom")