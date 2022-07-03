from math import cos, exp, sin, sqrt


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def _conver_to_complex(self, number):
        if not isinstance(number, ComplexNumber):
            return ComplexNumber(number, 0)
        return number

    def __neg__(self):
        return ComplexNumber(-self.real, -self.imaginary)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        c = self._conver_to_complex(other)
        real = self.real + c.real
        imaginary = self.imaginary + c.imaginary
        return ComplexNumber(real, imaginary)

    def __radd__(self, other):
        c = self._conver_to_complex(other)
        return self + c

    def __mul__(self, other):
        c = self._conver_to_complex(other)
        real = self.real * c.real - self.imaginary * c.imaginary
        imaginary = self.imaginary * c.real + self.real * c.imaginary
        return ComplexNumber(real, imaginary)

    def __rmul__(self, other):
        c = self._conver_to_complex(other)
        return c * self

    def __sub__(self, other):
        c = self._conver_to_complex(other)
        return self + (-c)

    def __rsub__(self, other):
        c = self._conver_to_complex(other)
        return c - self

    def __truediv__(self, other):
        c = self._conver_to_complex(other)
        real = (self.real * c.real + self.imaginary * c.imaginary) / (
            c.real**2 + c.imaginary**2
        )
        imaginary = (self.imaginary * c.real - self.real * c.imaginary) / (
            c.real**2 + c.imaginary**2
        )
        return ComplexNumber(real, imaginary)

    def __rtruediv__(self, other):
        c = self._conver_to_complex(other)
        return c / self

    def __abs__(self):
        return sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        r = round(cos(self.imaginary), 8) * exp(self.real)
        i = round(sin(self.imaginary), 8) * exp(self.real)
        return ComplexNumber(r, i)
