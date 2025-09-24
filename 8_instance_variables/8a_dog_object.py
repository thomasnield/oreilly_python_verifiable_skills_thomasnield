class Dog:  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
  
# Create an object  
my_dog = Dog("Buddy", 3)  
  
# Access instance variables  
print(my_dog.name)  # Output: Buddy  
print(my_dog.age)   # Output: 3  
  
# It's Buddy's birthday!  
# Let's modify his age my_dog.age += 1  
print(f"Buddy is now {my_dog.age} years old!")  
  
# Let's add a breed property  
# Note this is not a great practice, 
# but it demonstrates how *anything*
# can be mutated in Python
my_dog.breed = "Golden Retriever"  
print(f"Buddy is a {my_dog.breed}")