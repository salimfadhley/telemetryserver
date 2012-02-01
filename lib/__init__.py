import sys
import os
import logging
import site

log = logging.getLogger( __name__ )
libpath = os.path.dirname( os.path.abspath( __file__ ) )
site.addsitedir( libpath )