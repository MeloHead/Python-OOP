class Cup:
    def __init__(self, materialOfCup, colorOfCup):
        self.material = materialOfCup
        self.color = colorOfCup
        self.percent_filled = 0


def fill(self, amountOfLiquid):
    self.percent_filled += amountOfLiquid

def pour(self, amountOfLiquid):
    self.percent_filled -= amountOfLiquid

def spill(self):
    self.percent_filled = self.percent_filled / 2

def say_info(self):
    print(f"This {self.color} {self.material} cup is {self.percent_filled} % full")

myFavCup = Cup("plastic", "blue")
paper = Cup("paper", "white")

myFavCup.fill(60)
myFavCup.spill()
myFavCup.pour(13)
myFavCup.say_info()