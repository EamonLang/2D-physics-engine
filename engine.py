import time

class Object:
    # position,velocity, and force should all be tuples with 2 float numbers. One for x and one for y coordinates
    def __init__(self,position,velocity,mass,force):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.force = force

# contain math functions that determine outcomes of actions

class VectorMath:
    # addition functions
    @staticmethod
    def add_vector(pair1,pair2): 
        return (float(pair1[0])+float(pair2[0]),float(pair1[1])+float(pair2[1]))
    @staticmethod
    def add_scalar(pair,scalar):
        return (float(pair[0])+float(scalar),float(pair[1])+float(scalar))
    # Division functions
    @staticmethod
    def divide_scalar(pair1,scalar):
        # returns tuple of (first element in pair/mass , second element of pair/mass)
        return(float(pair1[0])/float(scalar),float(pair1[1])/float(scalar))
    
    @staticmethod
    def divide_vector(pair1,pair2):
        return (pair1[0]/pair2[0],pair1[1]/pair2[1])
    

    # multiplication functions
    @staticmethod
    def multiply_scalar(pair1,scalar):
        return (float(pair1[0])*scalar,float(pair1[1])*scalar)
    
    @staticmethod
    def multiply_vector(pair1,pair2):
        return (pair1[0]*pair2[0],pair1[1]*pair2[1])

    



    pass
class World(VectorMath):
    def __init__(self,objects):
        super().__init__()
        self.objects = [obj for obj in objects]

    pass

    def step(self,dt):
        # force of gravity
        f_gravity = (0,-9.8)
        for obj in self.objects:
            # force of gravity            
            obj.force = self.multiply_scalar(f_gravity,obj.mass)

            # change velocity and position
            obj.velocity = self.add_vector(obj.velocity,self.multiply_scalar(self.divide_scalar(obj.force,obj.mass),dt))
            obj.position = self.add_vector(obj.position,self.multiply_scalar(obj.velocity,dt))

            obj.force = (0,0)


obj  = Object((0,0),(0,0),1,(0,0))
earth = World([obj])

earth.step(1)

run = True
start_time = time.time()
while run:
    dt = time.time()
    earth.step(dt)
    print(obj.position)
    start_time = dt







    






    
        



