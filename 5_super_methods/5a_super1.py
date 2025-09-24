class MenuItem:  
    def __init__(self, name: str, price: float):  
        self.name = name  
        self.price = price  
  
    def get_description(self) -> str:  
        return f"{self.name}: ${self.price:.2f}"  
        
class Pastry(MenuItem):  
    def __init__(self, name: str, price: float, is_gluten_free: bool = False):  
        super().__init__(name, price)  # Initialize parent class attributes 
        self.is_gluten_free = is_gluten_free  
  
    def get_description(self) -> str:  
        base_description = super().get_description()  
        return f"{base_description}{' (GF)' if self.is_gluten_free else ''}"  
        
        
if __name__ == "__main__":  
    pastry = Pastry("Croissant", 2.00)  
    print(pastry.get_description())   
  
    gf_pastry = Pastry("Vanilla Bean Donut", 4.50, is_gluten_free=True)  
    print(gf_pastry.get_description())    