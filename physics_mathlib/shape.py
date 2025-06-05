from . import vector
from . import utils

class Object:
    def __init__(self,position,velocity,force,mass):
        self.position = vector.Vector2D(position[0],position[1])
        self.velocity = vector.Vector2D(velocity[0],velocity[1])
        self.force = vector.Vector2D(force[0],force[1])
        self.mass = float(mass)
    



class Circle(Object):
    def __init__(self, position, velocity, force, mass,radius):
        super().__init__(position, velocity, force, mass)
        self.radius = radius
        self.type = 'circle'
        self.inertia = 0.5* self.mass * (utils.square(self.radius))

        self.angle = 0
        self.angular_velocity = 0
        self.torque = 0
        


class Rect(Object):
    def __init__(self, position,velocity, force, mass,width,height):
        super().__init__(position, velocity, force, mass)
        self.type = 'rect'
        self.height = height
        self.width = width
        

