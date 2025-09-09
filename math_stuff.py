import math

radius = float(input())
height = float(input())

volume = math.pi * (radius ** 2) * height
area = (2 * math.pi * radius * height) + (2 * math.pi * (radius**2))

print(f'Volume: {volume:.1f} cubic inches')
print(f'Volume: {area:.1f} cubic inches')


user_int = int(input('Enter integer (32 - 126):\n'))
user_float = float(input('Enter float:\n'))
user_character = input('Enter character:\n')
user_string = input('Enter string:\n')
char_num = chr(user_int)

print(user_int, user_float, user_character, user_string)
print(user_string, user_character, user_float, user_int)
print(f'{user_int} converted to a character is {char_num}')

