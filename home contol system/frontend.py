import tkinter as tk
from tkinter import *
from backend import SmartHome, SmartPlug, CustomDevice

def setUpHome():
    # Create an instance of the SmartHome class
    smartHome = SmartHome()

    # Prompt the user to add five devices of their choice
    for i in range(5):
        device_type = input(f"Enter device type for device {i + 1} (SmartPlug or CustomDevice): ")
        if device_type.lower() == "smartplug":
            consumption_rate = int(input(f"Enter consumption rate for SmartPlug {i + 1}: "))
            smartPlug = SmartPlug(consumption_rate)
            smartHome.addDevice(smartPlug)
        elif device_type.lower() == "customdevice":
            option = input(f"Enter option for CustomDevice {i + 1}: ")
            customDevice = CustomDevice(option)
            smartHome.addDevice(customDevice)
        else:
            print("Invalid device type. Please enter 'SmartPlug' or 'CustomDevice'.")

    return smartHome

class SmartHomeSystem:
    def __init__(self, window, smartHome):
        self.window = window
        self.smartHome = smartHome
        self.window.resizable(False, False)
        self.window.title('FEROUS')
        self.window.geometry('700x500')

        self.device_frame = Frame(self.window, width=1000, height=500)
        self.device_frame.place(x=0, y=0)

        self.turn_on_all = Button(self.window, text="Turn on all", width=20, command=self.turnAllOn)
        self.turn_on_all.place(y=30, x=100)

        self.turn_off_all = Button(self.window, text="Turn off all", width=20, command=self.turnAllOff)
        self.turn_off_all.place(y=30, x=400)

        self.device_buttons = []

        for i, device in enumerate(self.smartHome.getDevices()):
            label = Label(self.window, text=f"Device {i + 1}: {device}")
            label.place(x=100, y=80 + i * 30)

            toggle_button = Button(self.window, text="Toggle", width=8, command=lambda i=i: self.toggleDevice(i))
            toggle_button.place(x=400, y=80 + i * 30)

            edit_button = Button(self.window, text="Edit", width=8, command=lambda i=i: self.editDevice(i))
            edit_button.place(x=470, y=80 + i * 30)

            delete_button = Button(self.window, text="Delete", width=8, command=lambda i=i: self.deleteDevice(i))
            delete_button.place(x=540, y=80 + i * 30)

            self.device_buttons.append((label, toggle_button, edit_button, delete_button))

        self.add_button = Button(self.window, text="Add", width=20, command=self.addDevice)
        self.add_button.place(y=80 + len(self.smartHome.getDevices()) * 30, x=100)

    def turnAllOn(self):
        self.smartHome.turnAllDevicesOn()
        self.updateGUI()

    def turnAllOff(self):
        self.smartHome.turnAllDevicesOff()
        self.updateGUI()

    def toggleDevice(self, index):
        device = self.smartHome.getDevice(index)
        device.toggleSwitch()
        self.updateGUI()

    def editDevice(self, index):
        device = self.smartHome.getDevice(index)
        # Open a new window for editing the device details
        # Implement this part based on your specific requirements

    def deleteDevice(self, index):
        device = self.smartHome.getDevice(index)
        self.smartHome.removeDevice(device)
        self.updateGUI()

    def addDevice(self):
        # Open a new window for adding a new device
        # Implement this part based on your specific requirements
        pass

    def updateGUI(self):
        for i, device in enumerate(self.smartHome.getDevices()):
            label, _, _, _ = self.device_buttons[i]
            label.config(text=f"Device {i + 1}: {device}")

def main():
    # Create an instance of the SmartHome class
    smartHome = setUpHome()

    # Create a Tkinter window
    window = tk.Tk()

    # Create a SmartHomeSystem object and pass the window and smartHome instance
    smartHomeSystem = SmartHomeSystem(window, smartHome)

    # Run the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    main()
