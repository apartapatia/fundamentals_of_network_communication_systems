from Polynomial import Polynomial

class BinaryVector:
    def __init__(self, vector_string):
        self.vector = [int(bit) for bit in vector_string]

    def __str__(self):
        return ''.join(str(bit) for bit in self.vector)

    def to_polynomial(self):
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