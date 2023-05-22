def jumlahnama(user_input):
    items = user_input.split(",")
    return len(items)


names = input("pls enter names separated with coma : ")
print(jumlahnama(names))