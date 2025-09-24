class Flyer:  
    def __init__(self, max_height):  
        self.max_height = max_height  
  
    def make_noise(self):  
        return "Whoosh!"  
  
  
class Swimmer:  
    def __init__(self, depth_limit):  
        self.depth_limit = depth_limit  
  
    def make_noise(self):  
        return "Splash!"  
  
  
class Duck(Flyer, Swimmer):  
    def __init__(self, max_height, depth_limit):  
        Flyer.__init__(self, max_height)  
        Swimmer.__init__(self, depth_limit)  
  
    def make_noise(self):  
        return "Quack!"  
  
  
duck = Duck(100, 0)  
  
print(f"max_height: {duck.max_height}")  
print(f"depth_limit: {duck.depth_limit}")  
print(f"make_noise: {duck.make_noise()}")