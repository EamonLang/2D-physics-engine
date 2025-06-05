from . import vector,utils,shape,collision

class World:
    def __init__(self,objects,width,height):
        super().__init__()
        self.objects_world = [obj for obj in objects]
        # height and width define the boundaries of the world
        self.width = width
        self.height = height

    pass

    def step(self,dt):
        # force of gravity
        f_gravity = vector.Vector2D(0,9.8)
        for index,obj in enumerate(self.objects_world):
            # check to see if object is within the world boundaries
            if obj.type == 'rect':
                if obj.position.x <= 0 or obj.position.x+obj.width >= self.width:
                    obj.velocity = vector.Vector2D(-1 * obj.velocity.x,obj.velocity.y)
                elif obj.position.y <= 0 or obj.position.y+obj.height >= self.height:
                    obj.velocity = vector.Vector2D(obj.velocity.x, -1*obj.velocity.y)
            
            if obj.type == 'circle':
                if obj.position.x-obj.radius <= 0 or obj.position.x + obj.radius>= self.width:
                    obj.velocity = vector.Vector2D(-1 * obj.velocity.x,obj.velocity.y)
                elif obj.position.y-obj.radius <= 0 or obj.position.y + obj.radius>=self.height:
                    obj.velocity = vector.Vector2D(obj.velocity.x, -1*obj.velocity.y)


            
            # check if there is a collision with the other objects
            for object in self.objects_world[index+1:]:
                
                collide = collision.detect_collision(obj,object)
                if collide:
                    collision.resolve_collision(obj,object)



            # force of gravity            
            obj.force = f_gravity.multiply_scalar(obj.mass)

            # change velocity and position
            obj.velocity = obj.force.divide_scalar(obj.mass).multiply_scalar(dt).__add__(obj.velocity)
            obj.position = obj.velocity.multiply_scalar(dt).__add__(obj.position)

            obj.force = vector.Vector2D(0,0)


