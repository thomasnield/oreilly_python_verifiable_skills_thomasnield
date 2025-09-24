x = "global"  # Global scope  
  
def outer():  
    x = "enclosing"    
	print(x)           

outer()
print(x)