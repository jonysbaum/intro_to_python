user_age_years = int(input('enter your age in years:\n'))

user_age_days = user_age_years  * 365
user_age_minutes = (user_age_days * 24) * 60
user_age_seconds = user_age_minutes * 60

print(f'You are at least {user_age_days} days old.')
print(f'You are at least {user_age_minutes} minutes old.')
print(f'You are at least {user_age_seconds} seconds old.')

print(f'Your heart has beat {72 * user_age_minutes} times.')

print (f'You have probably sneezed approximately {6 * user_age_days} times in your life.')

calories = 2300 * user_age_days
print(f'You have burned approximately {calories} calories in your life.')

# A peanut butter and jelly sandwich is 425 calories
sandwich = calories // 425

print(f'Which is about {sandwich} peanut butter and jelly sandwiches.')

# hours, minutes, seconds into just seconds
seconds = int(input())
minutes = int(input())
hours = int(input())

hours_in_seconds = (hours * 60) * 60
minutes_in_seconds =(minutes * 60)
total_time = hours_in_seconds + minutes_in_seconds + seconds
print(total_time)

# seconds into hours, minutes, and seconds
total_seconds = 4000 #int(input())

hours = (total_seconds // 60) // 60
minutes = (total_seconds // 60) - (hours * 60)
seconds = (((total_seconds / 60) - (hours * 60 )) - ((total_seconds // 60) - (hours * 60))) * 60

print(hours)
print(minutes)
print(seconds)