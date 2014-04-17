from time import sleep
from missionControl.rules import EventRecord

class TestEventRecord:

    def test_record_recordsHit(self):
        eventRecord = EventRecord()

        eventRecord.record()

        assert len( eventRecord.hits ) == 1

    def test_record_skips_ifNotOn(self):
        eventRecord = EventRecord()

        eventRecord.record( False )

        assert len( eventRecord.hits ) == 0

    def test_record_recordsLimitedHits(self):
        size = 5
        eventRecord = EventRecord( size )

        for c in range( 1, 2 * size ):
            eventRecord.record()

        assert len( eventRecord.hits ) == 5

    def test_hitsInTheLastNSeconds_returnsZeroIfAllExpired(self):
        eventRecord = EventRecord()
        eventRecord.record()
        sleep( .02 )

        assert eventRecord.hitsInTheLastNSeconds( .01 ) == 0

    def test_hitsInTheLastNSeconds_returnsCorrectCount(self):
        eventRecord = EventRecord()
        eventRecord.record()
        sleep( .02 )

        eventRecord.record()

        assert eventRecord.hitsInTheLastNSeconds( .01 ) == 1
