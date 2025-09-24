class CoffeeMenuItem:  
    def __init__(self, name, price, size):  
        self.name = name  
        self.price = price  
        self.size = size  

if __name__ == "__main__":  
	# Create two instances  
	latte = CoffeeMenuItem("Latte", 5.50, 20)  
	cold_brew = CoffeeMenuItem("Cold Brew", 4.50, 16)  
	  
	# Print attributes  
	print(f"Drink: {latte.name}, Price: ${latte.price}, Size: {latte.size}oz")  
	print(f"Drink: {cold_brew.name}, Price: ${cold_brew.price}, Size: {cold_brew.size}oz")