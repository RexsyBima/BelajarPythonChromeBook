import time

def tanggal(filepath):
    current_date = time.strftime('%Y-%m-%D %H:%M:%S')
    with open(filepath, 'a') as file:
        file.write(f"{current_date}")