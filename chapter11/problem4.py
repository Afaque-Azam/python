# create a class complex to represent complex number along with overloaded operator + and * which add and multiply them

class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self,c2):
        # (a + bi) + (c + di) = (a+c) + (b+d)i
        return Complex(self.r + c2.r, self.i + c2.i )
    
    def __mul__(self,c2):
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real_part = self.r * c2.r - self.i * c2.i
        img_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, img_part)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    

a = Complex(2,4)
b = Complex(4,6)

print("a + b =", a+b)
print("a x b =", a*b)