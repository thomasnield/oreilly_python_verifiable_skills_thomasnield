x = 10  
y = 5  
  
def combos(input_x, input_y):  
    collected_combos = []  
  
    for _x in range(0, input_x + 1):  
        for _y in range(0, input_y + 1):  
            collected_combos.append((_x, _y))  
  
    return collected_combos  
  
all_combos = combos(x, y)  
  
print(all_combos)