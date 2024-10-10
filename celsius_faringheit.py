class Temperature:

    temp = Temperature(25)

    def __init__(self, temp):
        self.__celsius = temp

    def to_fahrenheit(self, fahrenheit):
        self.fahrenheit = self.__celsius * 1.8 + 32
        print(fahrenheit)

    def get_celsius(self):
        return self.__celsius
        print(temp)









