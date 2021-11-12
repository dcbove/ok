import os
import json
import logging
import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ForkingMixIn

VERSION_FLAG = "delta"
ENV_FOO = os.environ.get("FOO", "<not set>")
ENV_PORT = int(os.environ.get("PORT", "5051"))

logging.getLogger().setLevel(logging.INFO)


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        message = json.dumps({
            "version": VERSION_FLAG,
            "datetime": str(datetime.datetime.now()),
            "environment": {
                "foo": ENV_FOO,
                "port": ENV_PORT
            }
        }, indent=4)

        self.wfile.write(bytes(message, "utf8"))


class ForkingHTTPServer(ForkingMixIn, HTTPServer):
    def finish_request(self, request, client_address):
        request.settimeout(30)
        HTTPServer.finish_request(self, request, client_address)


with ForkingHTTPServer(('', ENV_PORT), handler) as server:
    try:
        logging.info(f"Start server on {ENV_PORT}")
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
