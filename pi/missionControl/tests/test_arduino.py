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

    def test_lastWrite_returnsNoneIfNoMessages(self):
        serial = StubbedArduinoSerial()

        last = serial.getLastWrite()

        assert last is None


    def test_hasSent(self):
        serial = StubbedArduinoSerial()
        serial.write( 'test' )

        assert serial.hasSent( 'test' )

    def test_hasSent_returnsFalseIfMessageNotSent(self):
        serial = StubbedArduinoSerial()
        serial.write( 'test' )

        assert not serial.hasSent( 'test 2' )

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
        
    def test_setLed_on(self):
        serial = StubbedArduinoSerial()
        driver = ArduinoMatrixDriver(serial)

        driver.setLed( 'anLed', True )
        
        sent = serial.getLastWrite()
        assert sent == 'LED anLed on\n'
        
    def test_setLed_off(self):
        serial = StubbedArduinoSerial()
        driver = ArduinoMatrixDriver(serial)

        driver.setLed( 'anLed', False )
        
        sent = serial.getLastWrite()
        assert sent == 'LED anLed off\n'
        
