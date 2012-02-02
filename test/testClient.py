import xmlrpclib
import unittest

class ClientTest( unittest.TestCase ):
    
    def setUp(self):
        self.proxy = xmlrpclib.ServerProxy("http://localhost:8181/xml")

    def testRegister(self):
        print self.proxy.register(  "Salim Fadhley", "sal@stodge.org" )
        
    def testReRegister(self):
        uid0 = self.proxy.register( "Salim Fadhley", "sal@stodge.org" )
        uid1 = self.proxy.register( "Salim Fadhley", "sal@stodge.org" )
        assert uid0 == uid1, "Got different UIDs: %s != %s" % ( uid0, uid1 ) 
        
    def testSubmit(self):
        uid = self.proxy.register(  "Salim Fadhley", "sal@stodge.org" )
        assert isinstance( uid, str )
        submit_result = self.proxy.submit( uid, "temp", 0.0 )
        
    def testSubmitAndReadback(self):
        uid = self.proxy.register(  "Salim Fadhley", "sal@stodge.org" )
        assert isinstance( uid, str )
        
        STR_TEMP = "temp"
        
        self.proxy.submit( uid, STR_TEMP, 0.0 )
        self.proxy.submit( uid, STR_TEMP, 1.0 )
        self.proxy.submit( uid, STR_TEMP, 2.0 )
        
        results = self.proxy.getReadings( uid, STR_TEMP )
        
        assert len(results) == 3
        
if __name__ == "__main__":
    unittest.main()