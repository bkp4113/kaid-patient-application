#:::::::::::::::::::::::::::::::::::::::::::::#
# Author & Copyright : Bhaumik Patel
# Purpose: Flask Server to Run Patient
#          Application on default configured
#          PORT : 1990
#:::::::::::::::::::::::::::::::::::::::::::::#

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#______________________#
# Libs Import
#______________________#
import os
import sys
from urllib.error import HTTPError
from flask import Flask, request, send_from_directory, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import requests
import datetime, time

#______________________#
# App Import
#______________________#
print(sys.path)
from db import Patient, Roles, User
from database import db_session
from db import db
#______________________#
# App Setup and Load 
# Static File Path
# Default Upload Path
#______________________#
app = Flask(__name__)

#______________________#
# Serve Static Files
#______________________#
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/favicons/<path:path>')
def send_favicons(path):
    return send_from_directory('favicons', path)

def current_dt():
    return datetime.datetime.now().strftime("%m-%d-%Y_%H:%M:%S")
#______________________#
# Core Routes
#______________________#
@app.route("/paitent", methods=['GET'])
def create_paitent():
    current_dt = current_dt()
    if request.method == 'POST':
        try:
            data = request.get_json()
            
            return "SUCCESS!"
        except Exception as e:
            print (e)
            raise HTTPError('/uploadFiles', '500', 'Something went wrong on server!')

@app.route("/create_paitent", methods=['POST'])
def create_paitent():
    current_dt = current_dt()
    if request.method == 'POST':

        data = request.get_json()

        new = Patient('TEST','TEST')
        db_session.add(new)
        db_session.commit()

        if clientFile and appFile and allowed_file(clientFile.filename) and allowed_file(appFile.filename):
            try:
                uploadSuccess = "True"
            except Exception as e:
                print (e)
                raise HTTPError('/uploadFiles', '500', 'Something went wrong on server!')

@app.route("/create", methods=['POST'])
def create_paitent():
    current_dt = current_dt()
    if request.method == 'POST':

        clientFile = request.files['clientFile']
        appFile = request.files['appFile']

        if clientFile.filename == '' or appFile.filename == '':
            raise HTTPError('/uploadFiles','415', 'File seems to have no name!')

        if clientFile and appFile and allowed_file(clientFile.filename) and allowed_file(appFile.filename):
            try:

                uploadSuccess = "True"
            except Exception as e:
                print (e)
                raise HTTPError('/uploadFiles', '500', 'Something went wrong on server!')
    return uploadSuccess

@app.route("/login", methods=['POST'])
def login(client, username, password):

    try:
        return client.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)
    except HTTPError(code=403, msg"Not welcomed here!")

@app.route("/login", methods=['POST'])
def logout(client):
    return client.get('/logout', follow_redirects=True)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

def commit(action):

    if (action == 'add'):
        db.session.add(u)
    elif (action == 'query'):
        db.session.(u)
    elif (action == 'delete'):
        db.session.commit()

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='127.0.1.1', port='1990', use_reloader=False, use_debugger=True)