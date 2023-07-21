class Motorcycle:
    is_engine_on = False
    is_headlight_on = False
    make = None
    model = None
    is_driving = False

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return (f'{self.make} {self.model} with engine '
                f'{"on" if self.is_engine_on else "off"} and headlight '
                f'{"on" if self.is_headlight_on else "off"}')

    def turn_engine_on(self):
        print('Turning engine on')
        self.is_engine_on = True

    def turn_engine_off(self):
        print('Turning engine off')
        if self.is_driving:
            print('You tried to turn the engine off while driving, '
                  'and crashed')
            return

        self.is_engine_on = False

    def turn_headlght_on(self):
        print('Turning headlight on')
        self.is_headlight_on = True

    def turn_headlght_off(self):
        print('Turning headlight off')
        self.is_headlight_on = False

    def start_driving(self):
        if not self.is_engine_on:
            print("You can't drive without turning engine on!")


moto = Motorcycle('Triumph', 'Thruxton')
print(moto)
print(moto.is_engine_on)

moto.turn_engine_on()
print(moto.is_engine_on)
