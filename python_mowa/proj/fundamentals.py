print('P1')
miles = int(input("How far would you like to travel in miles ?\n" ))
if miles<3:
    print("Ride Bicycle")
elif miles > 3 and miles < 300:
    print("Use Motor Cycle")
elif miles> 300 :
    print("Use super car")

print("-------------------------------------------------------------")
print('P2')

per_hour=0.51
per_day=24*per_hour
per_week=7*per_day
per_month=30*per_week
for_918=int(918/per_day)
print(f'Server per day =  {per_day}')
print(f'Server per week = {per_week}')
print(f'Server per month = {per_month}')
print(f'You can operate {for_918} days with $918')
