from Polynomial import Polynomial
import random

class BinaryVector:
    def __init__(self, vector_string):
        self.vector = [int(bit) for bit in vector_string]

    def __str__(self):
        return ''.join(str(bit) for bit in self.vector)

    def to_polynomial(self):
        """
        Конвертирует в полином

        :return: полином из битового представления
        """
        polynomial_coeffs = self.vector
        return Polynomial(polynomial_coeffs)

    def __len__(self):
        return len(self.vector)

    def __add__(self, other):
        max_length = max(len(self), len(other))
        result = [0] * max_length

        for i in range(max_length):
            result[i] = self.vector[i] ^ other.vector[i]

        return BinaryVector(result)

    def error_coefficient(self, indices):
        """
        Инвертирует индексы

        :param indices: индекс, который необходимо инвертировать
        :return: новый вектор
        """
        for index in indices:
            if 0 <= index < len(self):
                self.vector[index] = 1 - self.vector[index]
            else:
                raise IndexError("Выход за пределы!")

    def random_indices(self, num_indices):
        """
        Генерирует случайные индексы для вектора

        Аргументы:
        num_indices (int): Количество случайных индексов, которые нужно сгенерировать.

        Возвращает:
        list: Список случайных индексов.
        """
        if num_indices > len(self.vector):
            raise ValueError("Количество индексов превышает размер вектора")

        return random.sample(range(len(self.vector)), num_indices)

    def error_random_coefficient(self, num_errors):
        """
        Инвертирует коэффициенты вектора по случайно сгенерированным индексам

        Аргументы:
        num_errors (int): Количество коэффициентов, которые нужно инвертировать.

        Возвращает:
        None
        """
        indices = self.random_indices(num_errors)
        for index in indices:
            self.vector[index] = 1 - self.vector[index]