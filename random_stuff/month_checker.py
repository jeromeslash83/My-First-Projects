def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(the_year, the_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if the_month is >12 or <1:
    return "Invalid month, try again."
  if is_leap(the_year) == False:
    return month_days[the_month - 1]
  else:
    if month_days[the_month -1] == 28:
      return 29
    else:
      return month_days[the_month - 1]  
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
