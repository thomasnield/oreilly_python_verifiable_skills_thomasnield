class Flyer:  
    def fly(self, speed, altitude):  
        if speed < 0 or altitude < 0:  
            raise ValueError('speed and altitude cannot be negative')  
  
        return f"Flying at {speed} mph at {altitude} altitude!"  
    
class Swimmer:  
    def swim(self, speed, depth):  
        if depth > 0:  
            raise ValueError("Depth must be zero or negative relative to surface.")  
        return f"Swimming at {speed} mph at {depth} ft depth!"
        
        
class Fish(Swimmer):  
    def glub(self):  
        return "Glub! Glub!"
        
class Duck(Flyer, Swimmer):  
    def quack(self):  
        return "Quack quack!"  
  
    def swim(self, speed, depth=0):  
        if depth != 0:  
            raise ValueError("Ducks can only swim on surface at depth 0.")  
        return super().swim(speed, depth)
        
        
  
if __name__ == "__main__":  
	print("FISH:")  
	fish = Fish()  
	print(fish.glub())  
	print(fish.swim(7,-10))  
	  
	print("DUCK")  
	duck = Duck()  
	print(duck.quack())  
	print(duck.fly(20, 30))  
	print(duck.swim(5))