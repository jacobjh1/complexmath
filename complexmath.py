import cmath
from math import atan2 as arctan, sin, cos, tan, pi, sqrt
from math import acos as arccos, asin as arcsin

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

''' pass degree '''
def to_rads (deg):
    return deg / 180 * pi

''' pass radian '''
def to_degs (rad):
    return rad / pi * 180

class Complex:
    ''' pass arguments according to constructor assuming forms:
            a + jb = a + bi
            r*e^θi = r ∠ θ (where phase = θ)
    '''
    def __init__ (self, a=0, b=0, r=0, phase=0):
        self._complex = complex(a, b)
        self._a = a
        self._b = b
        self._r = r
        self._phase = phase

    def __add__ (self, other):
        if isinstance(other, Complex):
            return CRect(self._a + other._a, self._b + other._b)            
            
        elif isinstance(other, complex):
            return self._complex + other

        elif isinstance(other, (int, float)):
            return CRect(self._a + other, self._b)

        else:
            raise TypeError('Complex.__add__:', type(other),
                            'incompatible with Complex type')
        
    def __radd__ (self, other):
        return self + other

    def __sub__ (self, other):
        if isinstance(other, Complex):
            return CRect(self._a - other._a, self._b - other._b)
        
        elif isinstance(other, complex):
            return self._complex - other

        elif isinstance(other, (int, float)):
            return CRect(self._a - other, self._b)

        else:
            raise TypeError('Complex.__sub__:', type(other),
                            'incompatible with Complex type')

    def __rsub__ (self, other):
        return -self + other

    def __neg__ (self):
        return CRect(-self._a, -self._b)

    def __mul__ (self, other):
        if isinstance(other, Complex):
            return CPolar(self._r * other._r, self._phase + other._phase, True).swap()
        
        elif isinstance(other, complex):
            return self._complex * other

        elif isinstance(other, (int, float)):
            return CPolar(self._r * other, self._phase, True).swap()

        else:
            raise TypeError('Complex.__mul__:', type(other),
                            'incompatible with Complex type')

    def __rmul__ (self, other):
        return self * other

    def __truediv__ (self, other):
        if isinstance(other, Complex):
            return CPolar(self._r / other._r, self._phase - other._phase, True).swap()
        
        elif isinstance(other, complex):
            return self._complex / other

        elif isinstance(other, (int, float)):
            return CPolar(self._r / other, self._phase, True).swap()

        else:
            raise TypeError('Complex.__div__:', type(other),
                            'incompatible with Complex type')

    def __rtruediv__ (self, other):
        if isinstance(other, complex):
            return other / self._complex
        elif isinstance(other, (int, float)):
            return CPolar(other, 0) / self
        else:
            raise TypeError('Complex.__rdiv__:', type(other),
                            'incompatible with Complex type')

    def __pow__ (self, other):
        if isinstance(other, (int, float)):
            return CPolar(self._r ** other, self._phase * other, True).swap()
        else:
            raise TypeError('Complex.__pow__:', type(other),
                            'incompatible with Complex type')

    def __str__ (self):
        return str(self._complex)[1:-1]

    def __repr__ (self):
        return f'Complex({self._a},{self._b},{self._r},{self._phase})'

    def __eq__ (self, other):
        if isinstance(other, Complex):
            return cmath.isclose(self._complex, other._complex)
            #return self._complex == other._complex
        elif isinstance(other, complex):
            return cmath.isclose(self._complex, other._complex)
            #return self._complex == other
        elif isinstance(other, (int, float)):
            return cmath.isclose(self._a, other)
            #return self._a == other
        else:
            raise TypeError('Complex.__eq__:', type(other),
                            'incompatible with Complex type')

    def __ne__ (self, other):
        try:
            return not self == other
        except:
            raise TypeError('Complex.__ne__:', type(other),
                            'incompatible with Complex type')

    ''' basic, use CRect/CPolar __str__ instead '''                   
    def get_rect (self):
        return (self._a, self._b)

    def to_rect (self):
        return CRect(self._a, self._b)

    def conj (self):
        return CRect(self._a, -self._b)

    ''' polar = exponential, also basic '''
    def get_polar (self):
        return (self._r, self._phase)

    def to_polar (self):
        return CPolar(self._r, self._phase, True).swap()

    def get_mag (self):
        return self._r

    def get_real (self):
        return self._a

    def get_imag (self):
        return self._b

class CRect(Complex):
    ''' pass only rectangular form '''
    def __init__ (self, a, b):
        r = (a**2 + b**2)**0.5
        #phase = pi/2 if (a == 0 and b > 0) else pi/-2 if (a == 0 and b < 0) \
        #             else arctan(b/a)
        phase = arctan(b, a)
        Complex.__init__(self, a, b, r, phase)

    def __str__ (self):
        return str(self._a) + ('-j' if self._b < 0 else '+j') +\
               str(abs(self._b))

    def __repr__ (self):
        return str(self)
        #return f'CRect({self._a}, {self._b})'

    '''
    same as __str__() except the precision (rounding) of the real and 
        imaginary parts can be specified:
    prec_real = number of decimal places to round the real part to
    prec_imag = optional number of decimal places to round the imaginary part to
        if None, then prec_imag = prec_real
    '''
    def str_round (self, prec_real, prec_imag = None):
        if prec_imag is None:
            prec_imag = prec_real
            
        return f"{self._a:.{prec_real}f}{'-j' if self._b < 0 else '+j'}" +\
               f"{abs(self._b):.{prec_imag}f}"

class CPolar(Complex):
    ''' pass only polar form (default degrees)'''
    def __init__ (self, r, phase, rad = False):
        self._in_radians = rad
        phase = phase if rad else (phase*pi/180)
        a, b = r*cos(phase), r*sin(phase)
        Complex.__init__(self, a, b, r, phase)

    def __str__ (self):
        phase = self._phase if self._in_radians else self._phase*180/pi
        return str(self._r) +'∠' + str(phase) +\
               ('' if self._in_radians else 'º')

    def __repr__ (self):
        return str(self)
        #in_rad = ', rad = False' if not self._in_radians else ''
        #return f'CPolar({self._r}, {self._phase}{in_rad})'

    '''
    same as __str__() except the precision (rounding) of the magnitude and 
        phase parts can be specified:
    prec_mag = number of decimal places to round the magnitude part to
    prec_phase = optional number of decimal places to round the phase part to
        if None, thne prec_phase = prec_mag
    '''
    def str_round (self, prec_mag, prec_phase = None):
        if prec_phase is None:
            prec_phase = prec_mag
        phase = self._phase if self._in_radians else self._phase*180/pi
    
        return f"{self._r:.{prec_mag}f}∠{phase:.{prec_phase}f}" +\
               ('' if self._in_radians else 'º')

    def get_units (self):
        return 'radians' if self._in_radians else 'degrees'

    def swap_units (self):
        self._in_radians = not self._in_radians
        return self

    def swap (self):
        return self.swap_units()
        
if __name__ == '__main__':    
    ''' EECS 70A HW #5 #9.63 Impedance simplication ''' 
    z1 = 20
    z2 = 10
    z3 = CRect(0, 15)

    za = (z1*z2 + z1*z3 + z2*z3)/z3
    zb = ((z1*z2 + z1*z3 + z2*z3)/z1)
    zc = ((z1*z2 + z1*z3 + z2*z3)/z2)

    z4 = (za*CRect(10, -16)) / (za + CRect(10,-16))
    z5 = (zb*CRect(10, -16)) / (zb + CRect(10,-16))
    z6 = z4+z5
    
    zT = CRect(8, -12) + ((zc * z6) / (zc + z6))
    
    assert zT==CRect(34.688358640636295, -6.930103639431186), 'something broke'

    rounding1 = CRect(3.1415, -6.2830)
    rounding2 = CPolar(2.718, pi/2, rad = True)
    assert rounding1.str_round(2) == '3.14-j6.28'
    assert rounding1.str_round(1, 2) == '3.1-j6.28'
    assert rounding1.str_round(6) == '3.141500-j6.283000'
    assert rounding2.str_round(2) == '2.72∠1.57'
    assert rounding2.str_round(1, 3) == '2.7∠1.571'
    assert rounding2.str_round(4) == '2.7180∠1.5708'
