checkpassword = [False, False, False]
user_password = input("Please enter your new password here : ")

if len(user_password) >= 8:
    checkpassword[0] = True
for char in user_password:
    if char.isdigit():
        checkpassword[1] = True
for char in user_password:
    if char.isupper():
        checkpassword[2] = True

    
print(checkpassword)

if checkpassword == [True, True, True]:
    print("Strong password")
else:
    print("weak password")