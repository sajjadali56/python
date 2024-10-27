class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, c):
        real = self.real + c.real
        imag = self.imag + c.imag

        return Complex(real, imag)
    
    def __sub__(self, c):
        real = self.real - c.real
        imag = self.imag - c.imag

        return Complex(real, imag)
    
    def __mul__(self, c):
        """(a + bi) * (c + di) = (ac - bd) + (ad + bc)i"""

        real = self.real * c.real - self.imag * c.imag
        imag = self.real * c.imag - self.imag * c.real

        return Complex(real, imag)
    
    def __truediv__(self, c):
        """    
        """
        tem = Complex(c.real, - c.imag)
        numerator = self * tem
        denominator = c.real ** 2 + c.imag ** 2 

        numerator.real /= denominator
        numerator.imag /= denominator

        return numerator

    def __str__(self):
        return f"{self.real} + {self.imag}i"

a = Complex(1, 3)
b = Complex(2, 4)
c = a + b
d = a - b
e = a * b
f = a / b

print(a, b)
print(c, d, e, f)