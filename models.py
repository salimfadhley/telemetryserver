from google.appengine.ext import db

class Source(db.Model):
    uid = db.StringProperty( "Unique ID" )
    contact = db.EmailProperty( )
    name = db.StringProperty("User's name")

class Reading(db.Model):
    readingSource = db.ReferenceProperty( Source , "Source", "source")
    value = db.FloatProperty(required=True)
    readingType = db.TextProperty(required=True)
    modtime = db.DateTimeProperty(required=True, auto_now=True,
    addtime = db.DateTimeProperty(required=True, auto_now_add=True )
  