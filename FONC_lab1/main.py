from BinaryVector import BinaryVector
from Polynomial import Polynomial

# Произведем разбор примеров из методички
# 1 - 2 шаг работы кодера
g_x = Polynomial([1, 0, 1, 1])
r = g_x.degree()
m_vec = BinaryVector([1, 0, 1, 0])
k = len(m_vec)
m_pol = m_vec.to_polynomial()

# Вычисление многочлена c(x) = m(x)x^r mod g(x)
_, c_x = (m_pol * Polynomial.x(r)).divide(g_x)

# 3 шаг работы кодера
# Вычисление многочлена a(x) = m(x)x^r + c(x)
a_x = (m_pol * Polynomial.x(r)) + c_x
# длина должны быть k + r
a_vec = a_x.to_binary_vector()

# работа декодера
# на входе g_x, a_vec, e_vec (вектор ошибки, случайно измененный a_vec)
e = BinaryVector("0110110")
e_vec = a_vec + e
b_vec = e_vec + a_vec
b_pol = b_vec.to_polynomial()

# 2 шаг
# вычисление s(x) = b(x) mod g(x)
_, s_x = b_pol.divide(g_x)

# произошли ошибки E = 1
E = s_x.err()


