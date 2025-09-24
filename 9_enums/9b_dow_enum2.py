from enum import Enum  
  
class DayOfWeek(Enum):  
    SUNDAY = 0  
    MONDAY = 1  
    TUESDAY = 2  
    WEDNESDAY = 3  
    THURSDAY = 4  
    FRIDAY = 5  
    SATURDAY = 6  
  
  
print("Let's loop through the days of week")  
  
for dow in DayOfWeek:  
    print(dow)  
  
print("\nLet's get the value SUNDAY")  
dayOfWeek = DayOfWeek.SUNDAY  
print(f"name: {dayOfWeek.name}")  
print(f"value: {dayOfWeek.value}")