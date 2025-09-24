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

if __name__ == "__main__":    
	fish = Fish() 
    print(fish.glub())  
    print(fish.swim(7,-10))