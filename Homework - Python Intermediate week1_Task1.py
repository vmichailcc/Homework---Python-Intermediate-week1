class StaticMethodsMixin:
    @staticmethod
    def add_static(fract1, fract2):
        num_stat = fract1.num * fract2.den + fract1.den * fract2.num
        den_stat = fract1.den * fract2.den
        return Fraction(num_stat, den_stat)

    @staticmethod
    def sub_static(fract1, fract2):
        num_stat = fract1.num * fract2.den - fract1.den * fract2.num
        den_stat = fract1.den * fract2.den
        return Fraction(num_stat, den_stat)

    @staticmethod
    def mul_static(fract1, fract2):
        num_stat = fract1.num * fract2.num
        den_stat = fract1.den * fract2.den
        return Fraction(num_stat, den_stat)

    @staticmethod
    def truediv_static(fract1, fract2):
        num_stat = fract1.num * fract2.den
        den_stat = fract1.den * fract2.num
        return Fraction(num_stat, den_stat)


class Fraction(StaticMethodsMixin):

    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        assert num != 0, 'Введите значение отличное от 0'
        self.__num = num

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, den):
        assert den > 0, 'Введите значение больше 0'
        self.__den = den

    def __sub__(self, other):
        newnum = self.num * other.den - other.num * self.den
        newnden = self.den * other.den
        return Fraction(newnum, newnden)

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newnden = self.den * other.den
        return Fraction(newnum, newnden)

    def __mul__(self, other):
        newnum = self.num * other.num
        newnden = self.den * other.den
        return Fraction(newnum, newnden)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newnden = self.den * other.num
        return Fraction(newnum, newnden)

    @classmethod
    def write(cls, line):
        num, den = map(int, line.split('/'))
        return cls(num, den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)


f1 = Fraction(3, 4)
print(f1.num)
f2 = Fraction(5, 6)
print(f"Сложение дробей = {f1+f2}")
print(f"Вычитание дробей = {f1-f2}")
print(f"Умножение дробей = {f1*f2}")
print(f"Деление дробей = {f1/f2}")

print(f"Сложение дробей (миксин) = {Fraction.add_static(f1, f2)}")
print(f"Вычитание дробей (миксин) = {Fraction.sub_static(f1, f2)}")
print(f"Умножение дробей (миксин) = {Fraction.mul_static(f1, f2)}")
print(f"Деление дробей (миксин) = {Fraction.truediv_static(f1, f2)}")

print(Fraction.write('2/5'))
