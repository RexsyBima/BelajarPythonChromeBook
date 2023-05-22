def x(year_of_birth, current_year):
    hasil = current_year - year_of_birth
    return hasil

year_of_birth = int(input("Please enter your birthyear : "))
if year_of_birth <= 120:
    print(str(x(year_of_birth, current_year=2023)))
else:
    print("aint no way fam ")