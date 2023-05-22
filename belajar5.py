feet_inches = input("enter feet and inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {'feet':feet, 'inches':inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

parsed = parse(feet_inches)
print(parse(feet_inches))
print(f"{parsed['feet']} ft {parsed['inches']} inch is equal to {convert(parsed['feet'], parsed['inches'])} meters")

conversion = float(input("enter how many liters to convert to cubic meterss : "))
def rubah(conversion):
    converted = conversion * 0.0001
    return converted

print(f"{rubah(conversion)} cubic meter")