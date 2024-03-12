from BinaryVector import BinaryVector
from Polynomial import Polynomial
import copy

# Задание параметров
g_x = Polynomial([1, 0, 1, 1]) * Polynomial([1, 1])
m_vec = BinaryVector("111")
m_x = m_vec.to_polynomial()
r = g_x.degree()
d = 4
k = 3
n = 7

# Вычисление многочлена c(x) = m(x)x^r mod g(x) - контрольная сумма
_, c_x = (m_x * Polynomial.x(r)).divide(g_x)

# Вычисление многочлена a(x) = m(x)x^r + c(x)
a_x = (m_x * Polynomial.x(r)) + c_x

# Проверка на делимость
_, reminder = a_x.divide(g_x)
print("Проверка на делимость пункт 1: ", reminder)  # выводится 0

# Пример работы декодера для случая, когда в канале
# произошло t ошибок при этом 1 <= t <= d - 1.
# Сделаем случайно 3 ошибки
a_vec_2 = a_x.to_binary_vector()
a_vec_2.error_random_coefficient(3)
a_x_edit = a_vec_2.to_polynomial()
_, reminder = a_x_edit.divide(g_x)
print("Случайно пункт 2: ", reminder)

# Сделаем вручную 2 ошибки
a_x_2 = copy.deepcopy(a_x)  # Клонируем многочлен a_x
a_x_2.coefficients[-2:] = [1, 1]  # Изменяем два последних коэффициента
_, reminder = a_x_2.divide(g_x)
print("Вручную пункт 2: ", reminder)

# Подбор t ошибок так, чтобы эти ошибки не обнаруживались,
# при этом t > d - 1. Количество ошибок может быть больше 3.
# Сделаем вручную 4 ошибки
a_x_edit = Polynomial([1, 1, 1, 0, 1])
_, reminder = a_x_edit.divide(g_x)
print("Вручную пункт 3:", reminder)

# Подбор t ошибок так, чтобы эти ошибки обнаруживались,
# при этом t > d - 1. Количество ошибок может быть больше 3.
# Сделаем случайно 4 ошибки
a_vec_3 = a_x.to_binary_vector()
a_vec_3.error_random_coefficient(5)
a_x_edit = a_vec_3.to_polynomial()
_, reminder = a_x_edit.divide(g_x)
print("Случайно пункт 4: ", reminder)

# Подбор t ошибок так, чтобы эти ошибки обнаруживались,
# при этом t > d - 1. Количество ошибок может быть больше 3.
# Сделаем вручную 4 ошибки
a_vec_4 = a_x.to_binary_vector()
a_vec_4.error_coefficient([3, 4, 5, 6])
a_x_edit = a_vec_4.to_polynomial()
_, reminder = a_x_edit.divide(g_x)
print("Вручную пункт 4: ", reminder)


# 5555555555555
m_5_vec = BinaryVector("11111")
m_5_x = m_5_vec.to_polynomial()
print(m_5_x)
# Вычисление многочлена c(x) = m(x)x^r mod g(x) - контрольная сумма
_, c_5_x = (m_5_x * Polynomial.x(r)).divide(g_x)
print(c_5_x)

# Вычисление многочлена a(x) = m(x)x^r + c(x)
a_5_x = (m_5_x * Polynomial.x(r)) + c_5_x

print(a_5_x)

a_edit_x = a_5_x.to_binary_vector()
a_edit_x.error_coefficient([0,7])
a_5_edit = a_edit_x.to_polynomial()
print(a_5_edit)
_, res = a_5_edit.divide(g_x)

print("Результат деления должен быть 0:", res, "На что делим: ", a_5_edit)
