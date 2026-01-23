import random
char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

while True:
    password_length = int(input('How long should the password be: '))
    
    if password_length < 4:
        print('Invalid')
        continue
    
    password = ''
    
    for i in range(password_length):
        password += random.choice(char)
            
    print('Generated Password:', password) 
    break