I am creating my own physics engine currently entirely in python. I have implemented basic physics including forces, acceleration, mass, position, and velocity. I hope to eventually be able to move this to c++ however I currently do not know the language.

I am following this article about how to create a physics engine in c++ however I am translating it to python.

Link for article: https://winter.dev/articles/physics-engine


For object-object collisions the math I used was from this article: https://www.vobarian.com/collisions/2dcollisions2.pdf

Currently the engine supports collision between to circles aswell as gravity. Next I would like incorporate more shapes aswell as develop my own math library.

You can use the window.py to render the engine aslong as you have pygame installed. Additionally in the future I hope to create my own sandbox allowing me to apply forces and create objects. Possibly within tkinter or pygame depending on what I want to render on.

NEXT STEPS:
    - friction
    - fluids
    - sandbox
    - c++??