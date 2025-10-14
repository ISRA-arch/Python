
class Instrument:
    def __init__(self, name, brand):
        self._name = name         
        self._brand = brand

    def play_sound(self):
        print(f"The {self._name} makes a pleasant sound 🎶")

    def info(self):
        print(f"Instrument: {self._name}, Brand: {self._brand}")


class Guitar(Instrument):
    def __init__(self, brand, strings):
        super().__init__("Guitar", brand)
        self.strings = strings

    
    def play_sound(self):
        print(f"Strumming the {self.strings}-string guitar 🎸")


class Drum(Instrument):
    def __init__(self, brand, size):
        super().__init__("Drum", brand)
        self.size = size

    def play_sound(self):
        print(f"Beating the {self.size}-inch drum 🥁")


class Piano(Instrument):
    def __init__(self, brand, keys):
        super().__init__("Piano", brand)
        self.keys = keys

    def play_sound(self):
        print(f"Playing the piano with {self.keys} keys 🎹")


class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def perform(self):
        print(f"{self.name} is performing now! 🌟")
        self.instrument.play_sound()

# 
