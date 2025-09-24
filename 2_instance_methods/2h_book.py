class Book:  
    def __init__(self, title, author, price):  
        self.title = title  
        self.author = author  
        self.price = price  
  
    def taxed_price(self, tax_rate=.07):  
        return self.price * (1.0 + tax_rate)  
  
if __name__ == "__main__":  
	book1 = Book("The Very Hungry Caterpillar", "Eric Carle", 5.00)  
	taxed_price = book1.taxed_price(tax_rate=.05)  
	  
	print(taxed_price)