x = 10  
y = 5  
  
def combos(x,y):  
    combos = []  
  
    for x in range(0,x+1):  
        for y in range(0,y+1):  
            combos.append((x,y))  
  
    return combos  
  
all_combos = combos(x,y)  
  
print(all_combos)