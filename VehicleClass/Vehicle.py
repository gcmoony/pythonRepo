
class Vehicle():

    def __init__(self, weight = 2000, color = "red", speed = 0):
        """
        Initializes new instance of class Vehicle.
        @param weight is the int weight of the Vehicle
        @param color is the str color of the Vehicle
        @param speed is the int speed of the Vehicle
        """
        self.weight = weight
        self.color = color
        self.speed = speed

    def speedUp(self, speedAmt):
        """
        Increase the vehicle's speed
        @param speedAmt the int amount the vehicle will travel
        in addition to the current speed.
        """
        self.speed += abs(speedAmt)

    def slowDown(self, speedAmt):
        """
        Decrease the vehicle's speed. Sets speed to '0' if
        the desired amount is larger than the current speed
        @param speedAmt the int amount the vehicle will travel
        subtracting from the current speed.
        """
        if speedAmt < self.speed:
            self.speed -= abs(speedAmt)
        else:
            self.speed = 0

    def getSpeed(self):
        """
        Returns an integer value of the vehicle speed
        """
        return self.speed

    def __str__(self):
        """
        Returns a string definition of the vehicle
        """
        desc = "This is a: " + str(type(self)) +\
        "\nThe weight is: " + str(self.weight) + " lbs" +\
        "\nThe color of the vehicle is: " + self.color
        return desc
