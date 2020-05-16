import Vehicle

class Boat(Vehicle.Vehicle):

    def __init__(self, weight = 2000, color = "Red", speed = 0,
    motorSize = 2.0):
        Vehicle.Vehicle.__init__(self, weight, color, speed)
        self.motorSize = motorSize

    def getMotorSize(self):
        return str(self.motorSize) + " Liter"
