print('Hello. Please input your score:')
grade = int(input('>'))
if grade >= 70:
    print('Your grade is A.')
elif grade >= 60:
    print('Your grade is B.')
elif grade >= 50:
    print('Your grade is C.')
elif grade >= 40:
    print('Your grade is D.')
else:
    print('You have failed')