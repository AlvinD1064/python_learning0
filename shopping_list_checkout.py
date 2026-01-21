total = 0

while True:
    price = float(input('Enter price: '))
    if price == 0:
        break
    elif price < 0:
        print('Invalid price.')
        continue
    else:
        total += price
        print('Current total is', total)
print('Final Total is', total)