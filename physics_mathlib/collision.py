
from . import vector
from . import utils

def detect_collision(obj1,obj2):
     combine_radius = obj1.radius + obj2.radius
     distance_between = obj1.position.distance_to(obj2.position)
     if distance_between <= combine_radius:
          return True
     else:
          return False

def resolve_collision(obj1,obj2):
              

            normal = obj1.position.__sub__(obj2.position)

            length_between = utils.pythagorean_theorem(normal.x,normal.y)

            unit_vector = normal.divide_scalar(length_between)

            unit_tangent = vector.Vector2D(-1*unit_vector.y , unit_vector.x)


            # in geometry could write a function for this
            object_normal__vector = obj1.velocity.multiply_vector(unit_vector)
            object_normal_velocity = object_normal__vector.x + object_normal__vector.y


            object_tangential__vector = obj1.velocity.multiply_vector(unit_tangent)
            object_tangential_velocity = object_tangential__vector.x +object_tangential__vector.y
            
            other_normal_vector = obj2.velocity.multiply_vector(unit_vector)
            other_normal_velocity = other_normal_vector.x + other_normal_vector.y
            

            other_tangential_vector = obj2.velocity.multiply_vector(unit_tangent)
            other_tangential_velocity = other_tangential_vector.x + other_tangential_vector.y
            

            final_scalar_velocity_object = (object_normal_velocity*(obj1.mass - obj2.mass) + 2*(obj2.mass*other_normal_velocity))/(obj1.mass+obj2.mass)
            final_scalar_velocity_other = (other_normal_velocity*(obj2.mass-obj1.mass)+(2*obj1.mass*object_normal_velocity))/(obj1.mass + obj2.mass)
            
            object_final_normal_velocity = unit_vector.multiply_scalar(final_scalar_velocity_object)
            object_final_tangential_velocity = unit_tangent.multiply_scalar(object_tangential_velocity)



            
            other_final_normal_velocity = unit_vector.multiply_scalar(final_scalar_velocity_other)
            other_final_tangential_velocity = unit_tangent.multiply_scalar(other_tangential_velocity)
            

            obj1.velocity = object_final_normal_velocity.__add__(object_final_tangential_velocity)
            obj2.velocity = other_final_normal_velocity.__add__(other_final_tangential_velocity)
