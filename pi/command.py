from time import sleep
import serial

class CommandFactory:
    def __init__(self):
        self.commands = {
            'P' : Potentiometer,
            'S' : Switch
        }

    def getCommand(self, parser):
        commandClass = self.commands.get( parser.token() )
        if commandClass:
            id = parser.next()
            value = parser.next()
            if id and value:
                return commandClass(id, value)

        return None

class Potentiometer:
    def __init__(self, id, potValue):
        self.id = id
        self.potValue = int( potValue )

    def applyRules(self, rules):
        potRule = rules.getPotRule(self.id)
        potRule(self.potValue)

class Switch:
    def __init__(self, id, value):
        self.id = id
        self.isOn = value.lower() in ( "yes", "true", "1", "t" )

    def applyRules(self, rules):
        switchRule = rules.getSwitchOnRule(self.id) if self.isOn else rules.getSwitchOffRule(self.id)
        switchRule()
