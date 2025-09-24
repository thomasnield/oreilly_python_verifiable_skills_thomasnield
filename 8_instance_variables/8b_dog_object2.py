class Dog:  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
  
    def set_age(self, age):  
        if age >= 0:  
            self.age = age  
        else:  
            raise ValueError("Age cannot be negative!")  
  
    def increment_age(self):  
        self.age += 1  
  
my_dog = Dog("Buddy", 3)  
my_dog.set_age(4)   
my_dog.increment_age()