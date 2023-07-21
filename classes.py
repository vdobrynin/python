class Motorcycle:
    is_engine_on = False
    is_headlight_on = False

    def turn_engine_on(self):
        self.is_engine_on = True


moto = Motorcycle()
print(moto)
print(moto.is_engine_on)

moto.turn_engine_on()
print(moto.is_engine_on)
