class Vetilador:

    @property
    def cor(self):
        return self.__cor.upper()

    @cor.setter
    def cor(self, new_color: str):
        if new_color.lower() == 'marinho':
            raise ValueError('Nao temos essa cor')
        self.__cor = new_color

    def __init__(self, color, power, voltage, price) -> None:
        self.__cor = color
