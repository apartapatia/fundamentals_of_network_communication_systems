from Polynomial import Polynomial

class BinaryVector:
    def __init__(self, vector_string):
        self.vector = [int(bit) for bit in vector_string]

    def __str__(self):
        return ''.join(str(bit) for bit in self.vector)

    def to_polynomial(self):
        polynomial_coeffs = self.vector
        return Polynomial(polynomial_coeffs)