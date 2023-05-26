shopping_list = []
price = []
quantity = []

def append_to_lists(shopping_list, list, price, harga, quantity, quantities):
    shopping_list.append(list)
    price.append(harga)
    quantity.append(quantities)


def add_to_lists(shopping_list, input_shopping, price, input_price, quantity, input_quantity):
    shopping_list.append(input_shopping)
    price.append(input_price)
    quantity.append(input_quantity)


def list_pops(shopping_list, price, quantity, input_hapus):
    shopping_list.pop(input_hapus)
    price.pop(input_hapus)
    quantity.pop(input_hapus)

def opendata_write(filepath):
    total_multiplied = [price * quantity for price, quantity in zip(price, quantity)]
    with open(filepath, 'w') as file:
        for i, (data,harga,jumlah) in enumerate(zip(shopping_list,price,quantity)):
            file.writelines(f"{str(i+1)}. {data} | harga = {harga} $| jumlah {jumlah} | total biaya item {harga * jumlah} $ \n")
        file.writelines(f"total harga adalah {sum(total_multiplied)} $ \n") 