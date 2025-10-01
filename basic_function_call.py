# def get_minutes_as_hours(orig_minutes):
#
#     hours = minutes / 60
#     return hours
#
# minutes = float(input())
# print(get_minutes_as_hours(minutes))
#
# def calc_total_inches(num_feet, num_inches):
#
#     total_inches = (12 * feet) + inches
#     return total_inches
#
# feet = int(input())
# inches = int(input())
# print('Total inches:', calc_total_inches(feet, inches))
#
# def calc_pyramid_volume(base_length, base_width, pyramid_height):
#     pyramid_area = length * width
#     pyramid_volume = (pyramid_area * height) / 3
#     return pyramid_volume
#
# length = float(input())
# width = float(input())
# height = float(input())
# print(f'Volume for {length} {width} {height} is: {calc_pyramid_volume(length, width, height):.2f}')
# def print_feet_inch_short(num_feet, num_inches):
#     print(f'{user_feet}\' {user_inches}\"')
#
# user_feet = int(input())
# user_inches = int(input())
# print_feet_inch_short(user_feet, user_inches)

def mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):
    hours_traveled = minutes_traveled / 60.0
    miles_traveled = hours_traveled * miles_per_hour
    return miles_traveled

miles_per_hour = float(input())
minutes_traveled = float(input())

print(f'Miles: {mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):f}')