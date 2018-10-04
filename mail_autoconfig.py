#!/usr/bin/env python3
import os
from flask import Flask, render_template, request, Response
app = Flask(__name__)

@app.route('/mail/config-v1.1.xml')
def tb_autoconf():
    domain = request.host.replace('autoconfig.', '')
    xml = render_template('template.xml', domain=domain)
    return Response(xml, mimetype='text/xml')

if __name__ == "__main__":
    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer(('127.0.0.1', int(os.environ['LISTEN_PORT'])), app)
    http_server.serve_forever()
