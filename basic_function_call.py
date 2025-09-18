def get_minutes_as_hours(orig_minutes):

    hours = minutes / 60
    return hours

minutes = float(input())
print(get_minutes_as_hours(minutes))