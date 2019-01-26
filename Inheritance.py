class Arman():

    def arman(self):
        print("I am drinking milk and")


class Milk():

    def drinking_milk(self):
        print("I am getting muscular")


class BodyBuilder(Arman, Milk):
    pass


body_builder = BodyBuilder()
body_builder.arman()
body_builder.drinking_milk()