x = 10  # Global scope  
y = 5   # Global scope  
  
def combos(x, y):  # Function parameters create local variables  
    combos = []  
  
    for x in range(0, x+1):  # Local 'x' shadows parameter 'x'  
        for y in range(0, y+1):  # Local 'y' shadows parameter 'y'  
            combos.append((x, y))  # Refers to loop variables 'x' and 'y'  
  
    return combos  
  
all_combos = combos(x, y)  # Calls function with global 'x' and 'y'  
  
print(all_combos)  # Built-in 'print' function, outputs results