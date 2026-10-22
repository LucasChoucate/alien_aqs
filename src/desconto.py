from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class IDesconto():
    def calcular(self, valor):
        raise NotImplementedError
    
class ICupom():
    def aplicar_cupom(self, codigo):
        raise NotImplementedError
    
class IVIP():
    def calcular(self, usuario):
        raise NotImplementedError



class DescontoNormal(IDesconto):
    def calcular(self, valor):
        return valor * 0.1  # 10% de desconto
    
class DescontoVIP(IDesconto, ICupom, IVIP):
    def calcular(self, valor):
        return valor * 0.2  # 20% de desconto

    def aplicar_cupom(self, codigo):
        return True

    def validar_usuario_vip(self, usuario):
        return usuario == "vip"

class DescontoPremium(Desconto):
    def calcular(self, valor):
        return valor * 0.3  # 30% de desconto

class CalculadoraDesconto:
    def __init__(self, desconto: Desconto):
        self.desconto = desconto  # Injetando a estratégia de desconto

    def calcular_desconto(self, valor):
        return valor - self.desconto.calcular(valor)

class Pedido:
    def __init__(self, desconto: IDesconto):
        self.desconto = desconto  # Injetando a estratégia de desconto

    def total(self, valor):
        return valor - self.desconto.calcular(valor)



def aplicar_desconto(desconto: IDesconto, valor: float) -> float:
    return desconto.calcular(valor)

def aplicar_cupom(cupom: ICupom, codigo: str) -> bool:
    return cupom.aplicar_cupom(codigo)

def main():
    valor = 100

    normal = DescontoNormal()
    vip = DescontoVIP()

    print("Desconto Normal:", aplicar_desconto(normal, valor))
    print("Desconto VIP:", aplicar_desconto(vip, valor))

    print("Cupom VIP:", aplicar_cupom(vip, "DESC123"))

    pedido_normal = Pedido(DescontoNormal())
    pedido_vip = Pedido(DescontoVIP())

    print("Total Pedido Normal:", pedido_normal.total(valor))
    print("Total Pedido VIP:", pedido_vip.total(valor))

if __name__ == "__main__":  # pragma: no cover
    main()