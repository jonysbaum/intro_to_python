speed_limit = int(input())
drive_speed = int(input())

ticket_worth = drive_speed - speed_limit

if speed_limit - drive_speed >= 10: #driving_speed slower than speed limit
     print(50)
elif 6 >= ticket_worth >= 20:
     print(75)
elif 21 >= ticket_worth >= 40:
    print(150)
elif ticket_worth > 40:
    print(300)
else:
    print(0)

time = input()
age = int(input())

if age < 4:
    print('free')
elif time == 'day' and age >= 4:
    print('$8')
elif time == 'night':
    if 4 <= age <= 16:
        print('$12')
    elif 17 <= age <= 54:
        print('$15')
    elif age >= 55:
        print('$13')