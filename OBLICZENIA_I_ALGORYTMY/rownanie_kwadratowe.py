import cmath

a = int(input("Type a variable: "))
b = int(input("Type b variable: "))
c = int(input("Type c variable: "))

delta = b*b-(4*a*c)

if delta == 0:
    x0 = -b/(2*a)
    print("x0 = ",x0)
else:
    x1 = ((-1)*b-cmath.sqrt(delta))/(2*a);
    print("x1 = ",x1)
    x2 = ((-1)*b+cmath.sqrt(delta))/(2*a);
    print("x2 = ",x2)
