class Engine:

    def __init__(self, volume, power, torque):
        self.__volume = volume
        self.__power = power
        self.__torque = torque

    def get_volume(self):
        return self.__volume

    def power(self):
        return self.__power

    def get_torque(self):
        return self.__torque


class car_composition:
    def __init__(self, make, model, volume, power, torque):
        self.__make = make
        self.__model = model
        self.__engine = Engine(volume, power, torque)
    #
    # def get_make(self):
    #     return self.__make
    #
    # def get_make(self):
    #     return self.__model
    #
    # def get_make(self):
    #     return self.__make
    #
    #
    #
    # def get_volume(self):
    #     return self.volume
    #
    # def power(self):
    #     return self.power
    #
    # def get_torque(self):
    #     return self.torque