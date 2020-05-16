import Vehicle

class Car(Vehicle.Vehicle):

    def __init__(self, weight = 2000, color = "red", speed = 0, wheels = 4):
        Vehicle.Vehicle.__init__(self, weight, color, speed)
        self.wheels = wheels

    def wheelAmt(self):
        return str(self.wheels) + "Wheels"
