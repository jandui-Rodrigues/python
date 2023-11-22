class Tv:
    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, new_volume):
        if (new_volume) > 99:
            raise ValueError('Nao e possivel aumentar o volume')
        elif (new_volume) < 1:
            raise ValueError('Nao e possivel diminuir o volume')
        self.__volume = new_volume
        print(new_volume)

    def aumentar_volume(self):
        try:
            self.volume += 1
        except ValueError as error:
            print(error.args[0])

    def diminuir_volume(self):
        try:
            self.volume -= 1
        except ValueError as error:
            print(error.args[0])

    def on_off(self):
        self.__on = not self.__on

    def get_on_off(self):
        return self.__on

    def get_chanel(self):
        return self.__channel

    def change_channel(self, new_channel):
        if new_channel > 99 or new_channel < 1:
            raise ValueError('Esse canal nao existe')
        self.__channel = new_channel

    def __init__(self, size):
        self.__volume = 99
        self.__on = False
        self.__channel = 1
        self.__size = size


new_tv_39 = Tv(39)
new_tv_39.diminuir_volume()
new_tv_39.diminuir_volume()
new_tv_39.on_off()
print(new_tv_39.get_on_off())
print(new_tv_39.get_chanel())
new_tv_39.change_channel(55)
print(new_tv_39.get_chanel())
new_tv_39.change_channel(552)
