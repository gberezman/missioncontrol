from port import Port
from time import sleep
from rules import Rules
from command import CommandFactory
import threading

port = Port(CommandFactory(), timeout = .5)
rules = Rules()

def eventLoop():

    print "Starting event loop"

    while True:
        try:
            command = port.readCommand()
            if not command:
                sleep( .1 )
                continue

            command.fire(port, rules)

        except KeyboardInterrupt:
            exit()

mainThread = threading.Thread( target = eventLoop )
mainThread.start()
