
class Calculadora:
    def __init__(self, A, B) -> None:
        self.A = A
        self.B = B
        pass

    def sumar(self):
        return self.A + self.B

    def restar(self):
        return self.A - self.B


    def mult(self):
        return self.A * self.B




calc = Calculadora(19, 3)

print(calc.sumar())
print(calc.restar())