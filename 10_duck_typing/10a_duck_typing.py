class Duck:  
    def __init__(self, name):  
        self.name = name  
  
    def quack(self):  
        print("Quack!")
        
        
class Person:  
    def __init__(self, name, occupation):  
        self.name = name  
        self.occupation = occupation  
  
    def quack(self):  
        print("Ahem, Quack!")
        

duck_imposter = Person("Carl", "Animal Sound Artist")
duck_imposter.quack()

