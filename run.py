import logging
from wsgiref.simple_server import make_server
from spyne.server.wsgi import WsgiApplication
from app import app

if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
    
    wsgi_app = WsgiApplication(app)

    server = make_server('127.0.0.1', 7789, wsgi_app)

    print("listening to http://127.0.0.1:7789")
    print("wsdl is at: http://localhost:7789/?wsdl")

    server.serve_forever()
