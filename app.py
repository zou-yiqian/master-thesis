from flask import Flask, render_template, make_response, send_from_directory
app = Flask(__name__)

@app.route('/lab1')
def lab1():
    vxml = render_template('lab1.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response
