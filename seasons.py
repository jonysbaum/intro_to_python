input_month = input()
input_day = int(input())
days_in_month = {
    "January": 31, "February": 28, "March": 31,
    "April": 30, "May": 31, "June": 30,
    "July": 31, "August": 31, "September": 30,
    "October": 31, "November": 30, "December": 31
}


season = ''
spring = ['March', 'April', 'May', 'June']
summer = ['June',  'July', 'August', 'September']
autumn = ['September', 'October', 'November', 'December']
winter = ['December', 'January', 'February', 'March']
boundary_months = ['March', 'June', 'September', 'December']
if input_month not in days_in_month:
    print("Invalid")
elif input_day < 1 or input_day > days_in_month[input_month]:
    print("Invalid")
else:
    if input_month in boundary_months:
        if input_month == 'March':
            if input_day < 20:
                season = "winter"
            else:
                season = "spring"
        if input_month == 'June':
            if input_day < 21:
                season = "spring"
            else:
                season = "summer"
        if input_month == 'September':
            if input_day < 22:
                season = "summer"
            else:
                season = "autumn"
        if input_month == 'December':
            if  input_day < 21:
                season = "autumn"
            else:
                season = "winter"
    elif input_month in spring:
        season = "Spring"
    elif input_month in summer:
        season = "Summer"
    elif input_month in autumn:
        season = "Autumn"
    else:
        season = "Winter"

print(season)