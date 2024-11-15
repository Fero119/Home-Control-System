# Task1
class SmartPlug:
    def __init__(self, consumptionRate):
        self.switchedOn = False
        self.consumptionRate = consumptionRate

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getSwitchedOn(self):
        return self.switchedOn

    def getConsumptionRate(self):
        return self.consumptionRate

    def setConsumptionRate(self, newRate):
        if 0 <= newRate <= 150:
            self.consumptionRate = newRate
        else:
            print("Invalid consumption rate. Rate must be between 0 and 150.")

    def __str__(self):
        return f"Switched On: {self.switchedOn}, Consumption Rate: {self.consumptionRate}"


def testSmartPlug():
    plug = SmartPlug(45)
    plug.toggleSwitch()
    print(f"Switched On: {plug.getSwitchedOn()}")
    print(f"Consumption Rate: {plug.getConsumptionRate()}")
    plug.setConsumptionRate(75)
    print(f"New Consumption Rate: {plug.getConsumptionRate()}")
    print(plug)


testSmartPlug()
print("----------------------------------------------------------------------------------------------")


# Task2
class CustomDevice:
    def __init__(self, option):
        self.switchedOn = False
        self.setOption(option)

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getSwitchedOn(self):
        return self.switchedOn

    def getOption(self):
        return self.option

    def setOption(self, option):
        # Replace this with your specific logic for handling the option
        self.option = option

    def __str__(self):
        return f"CustomDevice: switchedOn={self.switchedOn}, option={self.option}"


def testDevice():
    # Create an instance of your CustomDevice class.
    customDevice = CustomDevice("default_option")

    # Toggle the status of this device using the toggleSwitch method.
    customDevice.toggleSwitch()

    # Print the switchedOn instance variable using the appropriate accessor method.
    print("Switched On:", customDevice.getSwitchedOn())

    # Print the current value of the option instance variable. Then set it to a new value (of your choice). Next, print it again.
    print("Option:", customDevice.getOption())
    customDevice.setOption("new_option")
    print("New Option:", customDevice.getOption())

    # Print the CustomDevice object.
    print(customDevice)


# Run the test function
testDevice()

print("----------------------------------------------------------------------------------------------")


# task 3

class SmartHome:
    def __init__(self):
        self.devices = []

    def addDevice(self, device):
        self.devices.append(device)

    def removeDevice(self, device):
        self.devices.remove(device)

    def toggleDevice(self, device):
        device.toggleSwitch()

    def toggleAllDevices(self):
        for device in self.devices:
            device.toggleSwitch()

    def turnAllDevicesOn(self):
        for device in self.devices:
            device.switchedOn = True

    def turnAllDevicesOff(self):
        for device in self.devices:
            device.switchedOn = False

    def getDevices(self):
        return self.devices

    def getDevice(self, index):
        return self.devices[index]

    def __str__(self):
        device_info = ""
        for device in self.devices:
            device_info += f"{device}\n"
        return f"SmartHome with devices:\n{device_info}"


def testSmartHome():
    # Create an instance of the SmartHome class
    smartHome = SmartHome()

    # Create two instances of the SmartPlug class with consumption rates of 45
    smartPlug1 = SmartPlug(45)
    smartPlug2 = SmartPlug(45)

    # Create an instance of your custom device
    customDevice = CustomDevice("Option A")

    # Toggle the first plug, hence turning it on
    smartPlug1.toggleSwitch()

    # Set its consumption rate to 150
    smartPlug1.setConsumptionRate(150)

    # Set the consumptionRate of the second plug to 25
    smartPlug2.setConsumptionRate(25)

    # Add both plugs and the custom device to the smart home object
    smartHome.addDevice(smartPlug1)
    smartHome.addDevice(smartPlug2)
    smartHome.addDevice(customDevice)

    # Toggle the status of the second plug using the appropriate method of the smart home object
    smartHome.toggleDevice(smartPlug2)

    # Print the smart home object
    print(smartHome)

    # Turn on all devices in the smart home and print the smart home object again
    smartHome.turnAllDevicesOn()
    print(smartHome)

    # Remove the first device and print the smart home
    smartHome.removeDevice(smartPlug1)
    print(smartHome)


# Run the test function
testSmartHome()
