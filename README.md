# complexmath.py
A simple Python module that allows for arithmetic (+ - * / **) using polar and rectangular complex numbers

Motivation:
I was doing some circuits homework one day, and I realized that my TI-84 cannot do arithmetic with polar complex numbers accurately, even if the support 
is ostensibly there.
Python's support for complex numbers is a bit hit or miss. The built-in complex type is only rectangular, and the cmath polar numbers are insufficient.

Other Comments:
The implementation might be a bit funky, but I promise it works. I've used this for 2 or 3 classes' worth of complex number calculations.
(The reason for potentially awkward design choices is that I forced myself to use inheritance, and I didn't really remember Python inheritance at the time.)

Directions:
The following is what I wrote in the source code:

'''Directions:
    CRect(x, y) is the constructor for rectangular form
    CPolar(r, θ, rad = False) is the constructor for polar form
        tbh degrees is the default, but it converts to radians right away
        and uses radians in internal calculations. To convert between
        degrees and radians, do num.swap() and no need to reassign.
        
   To swap between rect and polar, do:
        num = num.to_rect() and
        num = num.to_polar()
        
   Most common math operations will work, and rectangular form or polar
    form does not matter.
        Add, subtract, divide, multiply, exponent (with each other or
        with ints/floats), along with == and !=
        There's also an option to get the conjugate, but it creates a new
        object, so you have to reassign.
        The one annoying thing is that mult/div will output in degrees
        no matter what.
'''
