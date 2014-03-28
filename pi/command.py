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

    def fire(self, port, rules):
        rule = rules.potRule.get(self.id)
        if rule:
            rule(port, self.potValue)

class Switch:
    def __init__(self, id, value):
        self.id = id
        self.isOn = value.lower() in ( "yes", "true", "1", "t" )

    def fire(self, port, rules):
        rule = rules.onRule.get( self.id ) if self.isOn else rules.offRule.get(self.id)
        if rule:
            rule()
