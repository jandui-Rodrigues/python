# Declaração

class car:
    spedd = 100


# construtor


class Exemplo:
    def __init__(self):
        print("Inicializando Exemplo")

    def __new__(cls, *args, **kwargs):
        print("Criando uma nova instância de Exemplo")
        instance = super().__new__(cls)
        return instance


class Liquidificador_contrutor:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.cor = cor
        self.potencia = potencia
        self.tensao = tensao
        self.ligado = False
        self.velocidade = 0
        self.velocidade_maxima = 3
        self.corrente_atual_no_motor = 0


meu_liquidificador = Liquidificador_contrutor("Azul", 200, 127, 200)
seu_liquidificador = Liquidificador_contrutor(
    cor="Vermelho", potencia=250, tensao=220, preco=100
)

# Encapsulamento e Abstração


class Liquidificador_Encapsulamento:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.cor = cor
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0

    def ligar(self, velocidade):
        if velocidade > self.__velocidade_maxima or velocidade < 0:
            raise ValueError(
                f"Velocidade deve estar entre 0 e {self.__velocidade_maxima}"
            )

        self.__velocidade = velocidade
        self.__corrente_atual_no_motor = (
            (self._potencia / self._tensao) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0

    def esta_ligado(self):
        return self.__ligado


liquidificador_vermelho = Liquidificador_Encapsulamento(
    "Vermelho",
    250,
    220,
    100
    )
liquidificador_vermelho.ligar(1)
print("Está ligado?", liquidificador_vermelho.esta_ligado())
# Está ligado? True
liquidificador_vermelho.desligar()
print("Está ligado?", liquidificador_vermelho.esta_ligado())
# Está ligado? False


# getter e setters


class Liquidificador:
    def get_cor(self):
        return self.__cor.upper()

    def set_cor(self, nova_cor):
        if nova_cor.lower() == "turquesa":
            raise ValueError("Não existe liquidificador turquesa")

        self.__cor = nova_cor

    def __init__(self, cor, potencia, tensao, preco):
        # Observe que usamos o setter para já validarmos o primeiro valor
        self.set_cor(cor)

        # Demais variáveis omitidas para este exemplo


liquidificador = Liquidificador("Azul", "110", "127", "200")

# print(f"A cor atual é {liquidificador.__cor}")
# AttributeError: 'Liquidificador' object has no attribute '__cor'

print(f"A cor atual é {liquidificador.get_cor()}")
# A cor atual é AZUL
liquidificador.set_cor("Preto")
print(f"Após pintarmos, a nova cor é {liquidificador.get_cor()}")
# Após pintarmos, a nova cor é PRETO


# Especificadores em python;

class Liquidificador_especificado:
    # Getter
    @property
    def cor(self):
        return self.__cor.upper()

    @cor.setter
    # Repare que é @cor.setter, e não @property.setter
    def cor(self, nova_cor):
        if nova_cor.lower() == "turquesa":
            raise ValueError("Não existe liquidificador turquesa")

        self.__cor = nova_cor

    def __init__(self, cor, potencia, tensao, preco):
        # Observe que usamos o setter para já validarmos o primeiro valor:
        # usamos self.cor, que chama o setter, e não self.__cor que manipula
        # o atributo diretamente
        self.cor = cor

        # Demais variáveis omitidas para este exemplo


liquidificador = Liquidificador_especificado("Rosa", "110", "127", "200")

print(liquidificador.cor)
# ROSA
liquidificador.cor = "Vermelho"
print(liquidificador.cor)
# VERMELHO
