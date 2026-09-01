from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class DescontoNormal(Desconto):
    def calcular(self, valor):
        return valor * 0.1  # 10% de desconto
    
class DescontoVIP(Desconto):
    def calcular(self, valor):
        return valor * 0.2  # 20% de desconto

class DescontoPremium(Desconto):
    def calcular(self, valor):
        return valor * 0.3  # 30% de desconto

class CalculadoraDesconto:
    def __init__(self, desconto: Desconto):
        self.desconto = desconto  # Injetando a estratégia de desconto

    def calcular_desconto(self, valor):
        return valor - self.desconto.calcular(valor)

def main():
    valor = 100

    print(f"Desconto Normal: {DescontoNormal().calcular(valor)}")
    print(f"Desconto VIP: {DescontoVIP().calcular(valor)}")
    print(f"Desconto Premium: {DescontoPremium().calcular(valor)}")

    print("\nValores com desconto:");

    print(f"Desconto Normal (calculadora): {CalculadoraDesconto(DescontoNormal()).calcular_desconto(valor)}")
    print(f"Desconto VIP (calculadora): {CalculadoraDesconto(DescontoVIP()).calcular_desconto(valor)}")
    print(f"Desconto Premium (calculadora): {CalculadoraDesconto(DescontoPremium()).calcular_desconto(valor)}")

if __name__ == "__main__":
    main()