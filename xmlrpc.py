import lib
import wsgi_xmlrpc
from controller import controller0
    
interface = controller0()
    
application = wsgi_xmlrpc.WSGIXMLRPCApplication( instance=interface )