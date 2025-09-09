highway_number = int(input())

if 1 <= highway_number <= 99:
    highway_type = 'primary'
elif 100 <= highway_number <= 999:
    highway_type = 'auxiliary'
else:
    highway_type = 'invalid'

odd_or_even = highway_number % 2
if odd_or_even == 0:
    direction = 'east/west'
elif odd_or_even == 1:
    direction = 'north/south'
else:
    direction = 'invalid'

if highway_type == 'invalid':
    print(f'{highway_number} is not a valid interstate highway number.')
elif highway_type == 'primary':
    print(f'I-{highway_number} is {highway_type}, going {direction}.')
elif highway_type == 'auxiliary':
    serves = highway_number % 100
    if serves == 0:
        print(f'I-{highway_number} is {highway_type}, going {direction}, '
              f'but does not serve a valid primary highway.')
    else:
        print(f'I-{highway_number} is {highway_type}, going {direction}, '
              f'serving I-{serves}.')