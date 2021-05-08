# -*- coding: utf-8 -*-
"""
Created on Sat May  8 20:41:29 2021

@author: Luke

HackerRank Problem - Classes: Dealing with Complex Numbers
"""

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, c):
        if isinstance(c, Complex):
            return Complex(self.real + c.real, self.imaginary + c.imaginary)
        else:
            raise TypeError('Expected a complex number. Received %s' % type(c))
    def __sub__(self, c):
        if isinstance(c, Complex):
            return Complex(self.real - c.real, self.imaginary - c.imaginary)
        else:
            raise TypeError('Expected a complex number. Received %s' % type(c))
    def __mul__(self, c):
        if isinstance(c, Complex):
            R = self.real * c.real - self.imaginary * c.imaginary
            I = self.real * c.imaginary + self.imaginary * c.real
            return Complex(R , I)
        else:
            raise TypeError('Expected a complex number. Received %s' % type(c))
    def __truediv__(self, c):
        if isinstance(c, Complex):
            conjugate = Complex(c.real, c.imaginary * -1)
            numerator = self * conjugate
            denominator = c * conjugate
            return Complex(numerator.real/denominator.real,numerator.imaginary/denominator.real)
        else:
            raise TypeError('Expected a complex number. Received %s' % type(c))

    def mod(self):
        mod = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(mod, 0.00)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

C1 = Complex(2, 1)

C2 = Complex(5, 6)

# Below is short hand for this: C3 = C1.__add__(C2)

C3 = C1 + C2

C3 = C2.mod()

print(C3)
