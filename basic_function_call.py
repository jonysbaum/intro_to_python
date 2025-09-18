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