import time
from physics_mathlib import vector,utils,shape

class Object:
    # position,velocity, and force should all be tuples with 2 float numbers. One for x and one for y coordinates
    def __init__(self,position,velocity,mass,force,radius):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.force = force
        self.radius = radius

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
    

    # collision detection
    @staticmethod
    def check_for_collision(obj1,obj2):
        both_radius = obj1.radius + obj2.radius
        distance_between = (((obj1.position[0]-obj2.position[0])**2) + ((obj1.position[1] - obj2.position[1])**2))**0.5 # this long ass equation is just pythagorean theorem to find distance between the two center points of the objects
        if distance_between<=both_radius:
            return True
        else:
            return False
    
    @staticmethod
    def collision_resolution(obj1,obj2):
        # 1. a) find normal vecotr. The vector between the two objects
        normal = (obj1.position[0] - obj2.position[0],obj1.position[1]-obj2.position[1])

        # 1. B) Find the unit vector

        # length between two objects
        length = (normal[0]**2 +normal[1]**2)**0.5

        unit_vector = (normal[0]/length,normal[1]/length)

        # 1. C) Find unit tangent
        unit_tangent = (-unit_vector[1],unit_vector[0])

        # 2. Find scalar projections for both normal and tangential

        # object 1
        obj1_normal_velocity = obj1.velocity[0]*unit_vector[0] + obj1.velocity[1]*unit_vector[1]
        obj1_tangential_velocity = obj1.velocity[0]*unit_tangent[0] + obj1.velocity[1]*unit_tangent[1]

        # object 2
        obj2_normal_velocity = obj2.velocity[0]*unit_vector[0] + obj2.velocity[1]*unit_vector[1]
        obj2_tangential_velocity = obj2.velocity[0]*unit_tangent[0] + obj2.velocity[1]*unit_tangent[1]

        # 3. Find new tangential and normal velocites. Since there is no friction tangential stays the same and we can use conservation of energy to solve for normal velocities

        final_scalar_velocity_obj1 = (obj1_normal_velocity*(obj1.mass - obj2.mass) + 2*(obj2.mass*obj2_normal_velocity))/(obj1.mass+obj2.mass)
        final_scalar_velocity_obj2 = (obj2_normal_velocity*(obj2.mass-obj1.mass)+(2*obj1.mass*obj1_normal_velocity))/(obj1.mass + obj2.mass)

        # 4 Convert scalar normal and tangential to vectors

        # obj1
        final_normal_velocity_vector_obj1 = (final_scalar_velocity_obj1*unit_vector[0],final_scalar_velocity_obj1*unit_vector[1])
        final_tangential_velocity_vector_obj1 = (obj1_tangential_velocity*unit_tangent[0],obj1_tangential_velocity*unit_tangent[1])

        # obj2

        final_normal_velocity_vector_obj2 = (final_scalar_velocity_obj2*unit_vector[0],final_scalar_velocity_obj2*unit_vector[1])
        final_tangential_velocity_vector_obj2 = (obj2_tangential_velocity*unit_tangent[0],obj2_tangential_velocity*unit_tangent[1])

        # 5. Sum normal and tangent so that you return back to x and y components

        obj1.velocity = (final_normal_velocity_vector_obj1[0]+final_tangential_velocity_vector_obj1[0] , final_normal_velocity_vector_obj1[1]+final_tangential_velocity_vector_obj1[1])
        obj2.velocity = (final_normal_velocity_vector_obj2[0]+final_tangential_velocity_vector_obj2[0] , final_normal_velocity_vector_obj2[1]+ final_tangential_velocity_vector_obj2[1])


class World(VectorMath):
    def __init__(self,objects,width,height):
        super().__init__()
        self.objects = [obj for obj in objects]
        # height and width define the boundaries of the world
        self.width = width
        self.height = height

    pass

    def step(self,dt):
        # force of gravity
        f_gravity = (0,9.8)
        for index,obj in enumerate(self.objects):
            # check to see if object is within the world boundaries
            if obj.position[0] <= 0 or obj.position[0] >= self.width:
                obj.velocity = (-1 * obj.velocity[0],obj.velocity[1])
            elif obj.position[1] <= 0 or obj.position[1] >= self.height:
                obj.velocity = (obj.velocity[0], -1*obj.velocity[1])

            
            # check if there is a collision with the other objects
            for object in self.objects[index+1:]:
                collision = self.check_for_collision(obj,object)
                if collision:
                    self.collision_resolution(obj,object)
                    print("True")



            # force of gravity            
            obj.force = self.multiply_scalar(f_gravity,obj.mass)

            # change velocity and position
            obj.velocity = self.add_vector(obj.velocity,self.multiply_scalar(self.divide_scalar(obj.force,obj.mass),dt))
            obj.position = self.add_vector(obj.position,self.multiply_scalar(obj.velocity,dt))

            obj.force = (0,0)


# obj  = Object((0,0),(0,0),1,(0,0))
# earth = World([obj])

# earth.step(1)

# run = True
# start_time = time.time()
# while run:
#     dt = time.time()
#     earth.step(dt)
#     print(obj.position)
#     start_time = dt







    






    
        



