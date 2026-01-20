password = '1064Tamarind'

for attempt in range(3):
    password = input('Enter Password: ')
    if password == '1064Tamarind':
        print('Correct password.')
        break
    else:
        print('Wrong password. Try again.')
else:
    print('No attempts left') 