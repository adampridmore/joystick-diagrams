'''Joystick Gremlin (Version ~13) XML Parser for use with Joystick Diagrams'''
from xml.dom import minidom
import functions.helper as helper
import adaptors.joystick_diagram_interface as jdi

class JoystickGremlin(jdi.JDinterface):

    def __init__(self,filepath):
    ## TRY FIND PATH
        jdi.JDinterface.__init__(self)
        self.file = self.parse_xml_file(filepath) ## Remove from instantiation > Make testable function with error handling (FolloW DCS_World Pattern)
        
        # New Attributes
        self.device_names = self.get_device_names()

        self.modes = None
        self.mode = None
        self.devices = None
        self.device = None
        self.currentdevice = None
        self.currentMode = None
        self.currentInherit = None
        self.inherit = None
        self.buttons = None
        self.buttonArray = None
        self.inheritModes = {}
        self.usingInheritance = False

    def get_device_names(self):
        self.devices = self.getDevices()
        deviceItems = []

        for item in self.devices:
            deviceItems.append(item.getAttribute('name'))

        return deviceItems

    def get_modes(self):
        self.devices = self.getDevices()
        profile_modes = []

        item = self.devices[0] # All Modes common across JG
        modes = item.getElementsByTagName('mode')
        for mode in modes:
            mode_name = mode.getAttribute('name')
            profile_modes.append(mode_name)

        return profile_modes


    def parse_xml_file(self, xml_file):
        return minidom.parse(xml_file)

    def createDictionary(self):
        self.devices = self.getDevices()
        helper.log("Number of Devices: {}".format(str(self.devices.length)), 'debug')

        for self.device in self.devices:
            self.currentdevice = self.getSingleDevice()
            self.modes = self.getDeviceModes()
            helper.log("All Modes: {}".format(self.modes))
            for self.mode in self.modes:
                self.currentInherit = self.hasInheritance()
                self.buttonArray = {}
                self.currentMode = self.getSingleMode()
                helper.log("Selected Mode: {}".format(self.currentMode), 'debug')
                self.buttons = self.getModeButtons()
                self.extractButtons()
                self.updateJoystickDictionary(self.currentdevice,
                                    self.currentMode,
                                    self.currentInherit,
                                    self.buttonArray
                                    )
        if self.usingInheritance:
            self.inheritJoystickDictionary()
            return self.joystick_dictionary
        else:
            return self.joystick_dictionary

    def getDevices(self):
        return self.file.getElementsByTagName('device')

    def getModeButtons(self):
        return self.mode.getElementsByTagName('button')

    def getDeviceModes(self):
        return self.device.getElementsByTagName('mode')

    def getSingleDevice(self):
        return self.device.getAttribute('name')

    def getSingleMode(self):
        return self.mode.getAttribute('name')

    def hasInheritance(self):
        inherit = self.mode.getAttribute('inherit')
        if inherit != '':
            if self.usingInheritance != True:
                self.usingInheritance = True
            return inherit
        else:
            return False

    def inheritedModes(self):
        return self.mode.getAttribute('name')

    def extractButtons(self):
        for i in self.buttons:
            if i.getAttribute('description') != "":
                self.buttonArray.update ({
                "BUTTON_" + str(i.getAttribute('id')):str(i.getAttribute('description'))
                })
            else:
                self.buttonArray.update ({
                "BUTTON_" + str(i.getAttribute('id')): self.no_bind_text
                })
        return self.buttonArray

    def getDeviceCount(self):
        return self.file.getElementsByTagName('device').length
