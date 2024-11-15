import tkinter as tk
from tkinter import *
from tkinter import messagebox, simpledialog, colorchooser
import csv

# Device base class with common attributes and methods
class Device:
    def __init__(self, switchedOn=False):
        self.switchedOn = switchedOn

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getSwitchedOn(self):
        return self.switchedOn

    def __str__(self):
        return f"Switched On: {self.switchedOn}"

# SmartPlug class inheriting from Device
class SmartPlug(Device):
    def __init__(self, consumptionRate):
        super().__init__()
        self.consumptionRate = consumptionRate

    def setConsumptionRate(self, newRate):
        if 0 <= newRate <= 150:
            self.consumptionRate = newRate
        else:
            print("Invalid consumption rate. Rate must be between 0 and 150.")

    def getConsumptionRate(self):
        return self.consumptionRate

    def __str__(self):
        return f"{super().__str__()}, Consumption Rate: {self.consumptionRate}"

# CustomDevice class inheriting from Device
class CustomDevice(Device):
    def __init__(self, option):
        super().__init__()
        self.option = option

    def setOption(self, option):
        self.option = option

    def getOption(self):
        return self.option

    def __str__(self):
        return f"{super().__str__()}, Option: {self.option}"

# SmartHome class managing a collection of devices
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

    def saveStateToFile(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for device in self.devices:
                if isinstance(device, SmartPlug):
                    writer.writerow(['SmartPlug', device.getConsumptionRate(), device.getSwitchedOn()])
                elif isinstance(device, CustomDevice):
                    writer.writerow(['CustomDevice', device.getOption(), device.getSwitchedOn()])

    def loadStateFromFile(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == 'SmartPlug':
                    consumptionRate = int(row[1])
                    switchedOn = bool(row[2])
                    self.devices.append(SmartPlug(consumptionRate))
                    if not switchedOn:
                        self.devices[-1].toggleSwitch()
                elif row[0] == 'CustomDevice':
                    option = row[1]
                    switchedOn = bool(row[2])
                    self.devices.append(CustomDevice(option))
                    if not switchedOn:
                        self.devices[-1].toggleSwitch()