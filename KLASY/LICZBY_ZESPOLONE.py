class Complex:
    def __init__(self, re, im=0.0):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.im * other.re + self.re * other.im)

    def __div__(self, other):
        self_re, self_im, other_re, oi = self.real, self.imag, other.real, other.imag
        r = float(other.re ** 2 + other.im ** 2)
        return Complex((self.re * other.re + self.im * other.im) / r, (self.im * other.re - self.re * other.im) / r)

    def print(self):
        if self.im != 0:
            print(f"Real = {self.re}, Imaginary=  {self.im}j\n")
        else:
            print(f"Real = {self.re}")



a = Complex(2,-14)
b = Complex(4,-2)

C = a + b
C.print()