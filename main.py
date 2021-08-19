#!/usr/bin/env python
import os

from flask import Flask, render_template, redirect
import requests

# Strings
app_description = "This is the english classes streaming project created by Igor Dzichkovskii for UKPIK Productions."
app_name = "UKPIK Productions: English Lessons"

app = Flask(app_name)


@app.route('/')
def index():
    return render_template("index.html", app_name=app_name, app_description=app_description)


@app.route('/test')
def test():
    return render_template("index.html", app_name=app_name, app_description=app_description)


@app.route('/igor')
def igor():
    return redirect("https://cloudnine13.github.io/IgorCV.pdf")


@app.after_request
def after_request(response):
    response.headers.add('Accept-Ranges', 'bytes')
    return response


if __name__ == '__main__':
    app.run()
