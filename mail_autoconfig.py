#!/usr/bin/env python3
from flask import Flask, render_template, request, Response
app = Flask(__name__)

@app.route('/mail/config-v1.1.xml')
def tb_autoconf():
    domain = request.host.replace('autoconfig.', '')
    xml = render_template('template.xml', domain=domain)
    return Response(xml, mimetype='text/xml')
