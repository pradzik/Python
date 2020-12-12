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
#problem with that method
    def __div__(self, other):
        r = float(other.re ** 2 + other.im ** 2)
        return Complex((self.re * other.re + self.im * other.im) / r, (self.im * other.re - self.re * other.im) / r)

    def print(self):
        if self.im != 0 and self.re != 0:
            print(f"Real = {self.re}, Imaginary=  {self.im}j\n")
        elif self.im == 0 and self.re != 0:
            print(f"Real = {self.re}")
        elif self.re == 0 and self.im != 0:
            print(f"Imaginary = {self.im}")
        else:
            print("Result = 0")


def complex_parse(s):
    l = len(s)
    if s.find('+') != -1:
        i = s.find('+')
    else:
        i = s.find('-')
    real = s[:i]
    if s[i] == "+":
        imaginary = s[i + 1:l - 1]
    else:
        imaginary = s[(i - 1) + 1:l - 1]
    return int(real), int(imaginary)


x = input("Type first number: ")

re_x, im_x = complex_parse(x)
complex_x = Complex(re_x, im_x)

s = input("Type math operation {/,*,-,+}: ")
y = input("Type second number: ")

re_y, im_y = complex_parse(y)
complex_y = Complex(re_y, im_y)

if s == "+":
    z = complex_x + complex_y
elif s == "-":
    z = complex_x - complex_y
elif s == "/":
    z = complex_x / complex_y
elif s == "*":
    z = complex_x * complex_y
else:
    z = "Wrong input"
z.print()
