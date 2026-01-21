savings = 0.0

while savings <= 50.0:
    deposit_amount = float(input('Enter deposit_amount: '))
    if deposit_amount < 0:
        print('Wrong value.')
        continue
    savings += deposit_amount
    print('Your current savings are:', savings)
print('You have reached your savings goal.')
        