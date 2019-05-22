import Vehicle
import Car

def printSpeed(aVehicle):
    print("Speed:", aVehicle.getSpeed(), "mph")

def main():
    # Variable Testing
    speedValues = [10, 20, 30, 40]
    vehColor = "Blue"
    vehWeight = 1000

    # Create Vehicle Instance
    myVeh = Vehicle.Vehicle(vehWeight, vehColor)
    print(myVeh)

    # Test Vehicle Instance
    printSpeed(myVeh)
    myVeh.speedUp(speedValues[2])
    printSpeed(myVeh)
    myVeh.slowDown(speedValues[2])
    printSpeed(myVeh)

    # Create Car Instance
    myCar = Car.Car()
    print(myCar)

    # Test Car Instance
    printSpeed(myCar)
    myCar.speedUp(speedValues[3])
    printSpeed(myCar)
    print(myCar.wheelAmt())

if __name__ == "__main__":
    main()
