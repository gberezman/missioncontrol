from missionControl.arduino import StubbedArduinoSerial, ArduinoMatrixDriver

class TestStubbedArduinoSerial:

    def test_defaultReadResponse_isNone(self):
        response = StubbedArduinoSerial().read()

        assert response is None

    def test_suppliedReadResponse_isReturned(self):
        serial = StubbedArduinoSerial()
        serial.setReadResponse( 'test' )

        response = serial.read()
    
        assert response == 'test'

    def test_lastWrite_defaultsToNone(self):
        serial = StubbedArduinoSerial()

        last = serial.getLastWrite()

        assert last == None

    def test_lastWrite_isRecorded(self):
        serial = StubbedArduinoSerial()
        serial.write( 'test' )

        last = serial.getLastWrite()

        assert last == 'test'

class TestArduinoMatrixDriver:

    def test_setMeter(self):
        serial = StubbedArduinoSerial()
        driver = ArduinoMatrixDriver(serial)

        driver.setMeter( 'aMeter', 10 )
        
        sent = serial.getLastWrite()
        assert sent == 'Meter aMeter 10\n'
        
    def test_ledOn(self):
        serial = StubbedArduinoSerial()
        driver = ArduinoMatrixDriver(serial)

        driver.ledOn( 'anLed' )
        
        sent = serial.getLastWrite()
        assert sent == 'LED anLed on\n'
        
    def test_ledOff(self):
        serial = StubbedArduinoSerial()
        driver = ArduinoMatrixDriver(serial)

        driver.ledOff( 'anLed' )
        
        sent = serial.getLastWrite()
        assert sent == 'LED anLed off\n'
        
