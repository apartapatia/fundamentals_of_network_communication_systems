from BinaryVector import BinaryVector
from Polynomial import Polynomial

p = Polynomial([1, 1, 1, 1, 0, 1])
p_1 = Polynomial([1, 0, 1, 0, 1])
p_2 = Polynomial([1,1,1])
p_3 = Polynomial([1,0,0])
print(p.__str__() + " / " + p_1.__str__())

print("Сумма", p + p_1)

quotient, remainder = p.divide(p_1)
print("Частное:", quotient)
print("Остаток:", remainder)

b = BinaryVector("111001")
print(b.to_polynomial().__str__())


