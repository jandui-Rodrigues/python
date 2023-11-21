from classe_object import Liquidificador_Encapsulamento
from ventilador import Vetilador


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.liquidificador = None
        self.fan = None

    def comprar_liquidificador(
              self, liquidificador: Liquidificador_Encapsulamento
            ):
        if liquidificador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= liquidificador.preco
            self.liquidificador = liquidificador

    def buy_fan(self, fan: Vetilador):
        if fan.price <= self.saldo_na_conta:
            self.saldo_na_conta -= fan.price
            self.fan = fan

    def __str__(self):
        if (self.ventilador):
            return f"{self.nome} - possui um ventilador."
        else:
            return f"{self.nome} - não possui um ventilador."


liquidificador_vermelho = Liquidificador_Encapsulamento(
    "Vermelho",
    250,
    220,
    100
    )
ventilador_azul = Vetilador('azul', 110, 110, 230)

pessoa_cozinheira = Pessoa("Jacquin", 1000)
pessoa_cozinheira.comprar_liquidificador(liquidificador_vermelho)
pessoa_cozinheira.buy_fan(ventilador_azul)
