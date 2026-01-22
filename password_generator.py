import random

while True:
    userInput = int(input('How long should the password be: '))
    if userInput < 4:
        print('Error')
        continue
        
    password = ''
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    
    for i in range(userInput):
        password = password + random.choice(chars)
    print(password)
    break