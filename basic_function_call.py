def get_minutes_as_hours(orig_minutes):

    hours = minutes / 60
    return hours

minutes = float(input())
print(get_minutes_as_hours(minutes))

def calc_total_inches(num_feet, num_inches):

    total_inches = (12 * feet) + inches
    return total_inches

feet = int(input())
inches = int(input())
print('Total inches:', calc_total_inches(feet, inches))

def calc_pyramid_volume(base_length, base_width, pyramid_height):
    pyramid_area = length * width
    pyramid_volume = (pyramid_area * height) / 3
    return pyramid_volume

length = float(input())
width = float(input())
height = float(input())
print(f'Volume for {length} {width} {height} is: {calc_pyramid_volume(length, width, height):.2f}')