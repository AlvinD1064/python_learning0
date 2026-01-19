print('Enter current balance:')
current_balance = float(input('>'))
print('Enter bundle price:')
bundle_price =  float(input('>'))
if current_balance >= bundle_price:
    print('Eligible to purchase bundle.')
else:
    print('Insufficient balance. Please add', str(bundle_price - current_balance))