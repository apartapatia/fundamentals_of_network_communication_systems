class Polynomial:
    def __init__(self, coefficients):
        """
        Конструктор класса
        :param coefficients: Список булевых коэффицентов многочлена.
        """
        self.coefficients = coefficients

    def __str__(self):
        """
        Преобразование многочлена в строку.
        :return: Строковое представление многочлена
        """
        terms = []
        index = len(self.coefficients) - 1
        for i in range(len(self.coefficients) - 1, -1, -1):
            if self.coefficients[i]:
                if i == len(self.coefficients) - 1:
                    terms.append("1")
                else:
                    if index - i == 1:
                        terms.append(f"x")
                    else:
                        terms.append(f"x^{index - i}")
        return " + ".join(terms[::-1])

    def __len__(self):
        """
        Получение длины полинома.
        :return: Длина полинома (количество ненулевых коэффициентов)
        """
        return len(self.coefficients)

    def __getitem__(self, key):
        """
        Получение коэффициента полинома по индексу.
        :param key: Индекс
        :return: Коэффициент полинома по указанному индексу
        """
        return self.coefficients[key]

    def divide(self, divisor):
        """
        Деление многочлена на divisor по полю 2
        :param divisor: Другой полином, на который нужно разделить данный полином
        :return: Результат деления (частное и остаток)
        """
        dividend = self.coefficients[:]
        quotient = [0] * (len(dividend) - len(divisor) + 1)

        while len(dividend) >= len(divisor):
            exp_difference = len(dividend) - len(divisor)
            quotient[exp_difference] = dividend[0]

            for i in range(len(divisor)):
                dividend[i] ^= (divisor[i] & quotient[exp_difference])

            while len(dividend) > 0 and dividend[0] == 0:
                dividend.pop(0)

        remainder = dividend
        return Polynomial(quotient[::-1]), Polynomial(remainder)

    def degree(self):
            """
            Вычисление степени многочлена
            :return: степень многочлена
            """
            for i in range(len(self.coefficients) -1, -1, -1):
                if self.coefficients[i] == 1:
                    return i

    def __add__(self, other):
        """
        Сумма полиномов
        :param other: суммирующий полином
        :return: сумма полиномов
        """
        max_length = max(len(self), len(other))
        result = [0] * max_length

        for i in range(max_length):
            c_1 = self.coefficients[::-1][i] if i < len(self) else 0
            c_2 = other.coefficients[::-1][i] if i < len(other) else 0
            if c_1 != c_2:
                result[i] = 1

        return Polynomial(result[::-1])

