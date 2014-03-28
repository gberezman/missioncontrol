from port import Port
from time import sleep
from rules import Rules
import threading

port = Port(timeout = .5)
rules = Rules(port)

def eventLoop():

    print "Starting event loop"

    while True:
        try:
            command = port.readline()
            if not command:
                sleep( .1 )
                continue

            if command.token() == "P":
                pot = command.next()
                if pot:
                    command.next()
                    value = command.tokenAsInt()
                    if value:
                        print "pot {} = {}".format(pot, value)
                        rules.potEvent(port, pot, value)

            elif command.token() == "S":
                switch = command.next()
                if switch:
                    command.next()
                    isSwitchOn = command.tokenAsBoolean()
                    if isSwitchOn:
                        print "switch {} is {}".format(switch, isSwitchOn)
     
                        if isSwitchOn:
                            rules.switchOn( switch )
                        else:
                            rules.switchOff( switch )
            else:
                pass

        except KeyboardInterrupt:
            exit()

mainThread = threading.Thread( target = eventLoop )
mainThread.start()
