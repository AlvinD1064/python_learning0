print('Hello. Please input your score:')
grade = int(input('>'))
if grade >= 70:
    print('Grade: A')
elif grade >= 60:
    print('Grade: B')
elif grade >= 50:
    print('Grade: C')
elif grade >= 40:
    print('Grade: D')
else:
    print('Fail')