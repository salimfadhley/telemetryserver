from models import Source, Reading
from google.appengine.ext import db
from utils.id import mk_id
import logging

log = logging.getLogger(__name__)

class controller0( object ):
    
    @classmethod
    def register( cls, name, email, uid=None ):
        """
        Register a new account.
        """
        if uid==None:
            _uid = mk_id()
        else:
            _uid = uid
        log.warn( "New registration: Name=%s, email=%s, uid=%s" % ( name, email, uid ) )
        newAccount = Source( uid=_uid,
                             name=name,
                             email=email )
        
        newAccount.put()
        return newAccount.uid
        
    @classmethod
    def submit( cls, uid, readingType, readingValue ):
        assert isinstance( uid, str )
        assert isinstance( readingType, str )
        assert isinstance( readingValue, float )
        
        source = cls.getSource( uid )
        
        reading = Reading( readingSource=source,
                           value=readingValue,
                           readingType=readingType )
        
        reading.put()
        
        return reading.addtime
    
    @classmethod
    def getSource(cls, uid):
        assert isinstance( uid, str )
        s = Source.all()
        s.filter( "uid =", uid )
        results = [a for a in s.fetch( limit=1 ) ]
        assert len(results) > 0, "Could not find source record."
        return results[0]
    
    @classmethod
    def _getReadings(cls, uid, readingType ):
        """
        Get all the readings of a particular type
        """
        source = cls.getSource( uid )
        
        r = Reading.all()
        r.filter( "readingSource =", source )
        r.filter( "readingType =", readingType )
        r.order("-adddate")
        return [ re for re in r ]
    
    @classmethod
    def getReadings(cls, uid, readingType ):
        readings = cls._getReadings( uid, readingType )
        
        results = []
        
        for r in readings:
            import pdb
            pdb.set_trace()
        
        