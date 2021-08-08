#
# coseos-python3-sanic-example
#
# Copyright (c) 2021 <a href="https://coseos.com/">coseos</a>
#
# All righs reserved.
#

from sanic import Sanic
from sanic.response import json, html, text

app = Sanic(name='coseos-python3-sanic-example')

@app.route("/")
async def test(request):
    return html("""
        <html>
            <head>
                <meta charset="utf-8">
                <title>coseos Python3 Sanic example</title>
                <link rel="stylesheet" href="static/index.css">
            </head>
            <body>
                <h1>coseos Python3 Sanic example</h1>
                <p>
                    A Python 3 project using Sanic to implement a web server. This is a template to get you started with Python 3 and Sanic
                </p>
                <h2>License</h2>
                <p>
                    This software is provided with the <a href="https://www.apache.org/licenses/LICENSE-2.0.html">Apache License 2.0</a>
                </p>
                <h2>Support</h2>
                <p>
                    This template is provided by <a href="https://coseos.com/">coseos</a> / K2IT Gesellschaft für Informationstechnik mbH, Germany
                </p>
                <p>
                    Please contact us for training in software development and to get support for your software development projects
                </p>
            </body>
        </html>
    """)

@app.route("data")
async def test(request):
    return json({"name": "coseos-python3-sanic-example"})

if __name__ == '__main__':
    app.static('/static', './static')
    app.run(host="0.0.0.0", port=8181)
