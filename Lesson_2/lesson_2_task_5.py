def month_to_season(month):
  if month in (12,1,2):
     return "Winter"
  elif month in (3,4,5):
     return "Spring"
  elif month in (6,7,8):
      return "Summer"
  elif month in (9,10,11):
      return "Autumn"
  else:
      return "Wrong number of month"
  
  
print(month_to_season(1))
print(month_to_season(4))
print(month_to_season(8))
print(month_to_season(11))
print(month_to_season(15))
