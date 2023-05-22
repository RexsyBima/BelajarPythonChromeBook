inputtemp = input("Enter water temperature here : ")
inputtemp = int(inputtemp)

def temp(inputtemp):
    if inputtemp < 0:
        status = "Solid"
    elif inputtemp > 100:
        status = "Gas"
    elif 0 < inputtemp < 100:
        status = "Liquid"
    return status


print(temp(inputtemp))