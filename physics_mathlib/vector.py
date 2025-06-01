from . import utils

class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return Vector2D(self.x + other.x,self.y + other.y)
    
    def __sub__(self,other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def add_scalar(self,scaler):
        return Vector2D(self.x + scaler, self.y +scaler)
    
    def multiply_scalar(self,scalar):
        return Vector2D(self.x*scalar,self.y *scalar)
    
    def multiply_vector(self,other):
        return Vector2D(self.x*other.x,self.y*other.y)
    
    def divide_scalar(self,scalar):
        return Vector2D(self.x/scalar,self.y/scalar)
    
    def distance_to(self,other):
        normal = self.__sub__(other)
        return utils.pythagorean_theorem(normal.x,normal.y)
    
    def magnitude(self):
        return utils.pythagorean_theorem(self.x,self.y)
    

    
