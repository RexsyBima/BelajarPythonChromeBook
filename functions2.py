from functions import *
from tanggal import *

def load_data():
    shopping_list, price, quantity = [], [], []
    with open("data.txt", "r+") as file:
        for line in file:
            if not line.startswith("total") and not line.startswith("2023"):
                list_item = line.split("|")[0].split(".")[1].strip() 
                harga = int(line.split("|")[1].split("=")[1].strip().split(" ")[0])
                quantities = int(line.split("|")[2].split(" ")[2].strip())
                append_to_lists(shopping_list, list_item, price, harga, quantity, quantities)
    return shopping_list, price, quantity

def today_date():
    date = f"today's date is {time.strftime('%d %b %Y')}"
    return date
def app_name():
    name = "this is a shopping list application"
    return name

def creator():
    created = "Made by Rexsy Bima TW"
    return created

def input_loop(shopping_list, price, quantity):
    while True:   
        input_shopping = input("what are you plan to buy, input 0 to finish the list : ")
        if input_shopping == "0":
            print("Okay")
            break

        input_price = int(input("price in dollar : "))
        input_quantity = int(input("quantities : "))

        add_to_lists(shopping_list, input_shopping, price, input_price, quantity, input_quantity)

def save_data():
    filepath = 'data.txt'
    opendata_write(filepath)
    tanggal(filepath)
    exit("saved")

def print_list(shopping_list, price, quantity):
    for i, (item,item_price,item_quantity) in enumerate(zip(shopping_list, price, quantity)):
        print(f"{i+1}. nama barang = {item} | price = {item_price} $ | quantity = {item_quantity} | total items price = {item_price * item_quantity} $")
    total_multiplied = [price * quantity for price, quantity in zip(price, quantity)]
    print(f"the total cost is {sum(total_multiplied)} $")

def edit_list(shopping_list, price, quantity):
    while True:
        input_edit = int(input("in number, what plan to buy you want to remove, enter 0 to back to main menu : ")) - 1
        temp_edit = shopping_list[input_edit]
        if input_edit == -1:
            break
        shopping_list[input_edit] = input("what do you want change into : ")
        price[input_edit] = int(input("please enter the new price : "))
        quantity[input_edit] = int(input("please enter the new quantity : "))
        print(f"okay, shopping list number {input_edit+1}, {temp_edit} has been changed to {shopping_list[input_edit]}")
        if quantity[input_edit] == 1:
            print(f"the price is now {price[input_edit]} $ and there is {quantity[input_edit]} quantity. The total price is {price[input_edit] * quantity[input_edit]} $")
        elif quantity[input_edit] > 1:
            print(f"the price is now {price[input_edit]} $ and there is {quantity[input_edit]} quantities. The total price is {price[input_edit] * quantity[input_edit]} $")

def delete_from_list(shopping_list, price, quantity):
    while True:
        input_hapus = int(input("in number, what items you want to delete. enter 0 to back to main menu")) - 1
        if input_hapus == -1:
            break
        temp_hapus = shopping_list[input_hapus]
        list_pops(shopping_list, price, quantity, input_hapus)
        print(f"item {temp_hapus} telah dihapus")

def main():
    shopping_list, price, quantity = load_data()
    while True:
        try:
            user_input = int(input("press 1 to add, 2 to save, 3 to show and total cost, 4 to edit, 5 to delete items: "))
            if user_input == 1:
                input_loop(shopping_list, price, quantity)
            elif user_input == 2:
                save_data()
            elif user_input == 3:
                print_list(shopping_list, price, quantity)
            elif user_input == 4:
                edit_list(shopping_list, price, quantity)
            elif user_input == 5:
                delete_from_list(shopping_list, price, quantity)
            else:
                print("the input is incorrect")
        except ValueError:
            print("Incorrect input")

if __name__ == '__main__':
    main()