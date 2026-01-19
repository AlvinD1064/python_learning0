print('Hello dear customer. What is your bill amount?')  #ask customer for bill amount
amount = float(input('>'))
tip = round(amount * 0.1, 2)   #tip is 10% of bill amount
bill_total = round(amount + tip, 2)  #add tip to bill
print('Your calculated tip is', tip)
print('Your total bill is', bill_total)
print('Thank you for dining with us!')