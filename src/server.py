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
import requests
import json
import datetime, time
from urllib.error import HTTPError
from flask import Flask, request, redirect, url_for, jsonify
from flask_cors import cross_origin

#______________________#
# App Import
#______________________#
from db.database import db_session
from model.paitent import Patient
from model.user import User, Roles
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

def validate_args_fields(fields, args):

    status = True

    for keys in args.keys():
        if keys not in fields:
            passed = False

    return status

#______________________#
# Core Routes
#______________________#
@app.route("/paitent", methods=['GET', 'POST', 'PUT', 'DELETE'])
@cross_origin()
def paitent():

    request_url = request.url
    request_arg = dict(request.args)
    paitent_fields = ['first_name', 'middle_name', 'last_name', 'dob', 'gender']

    if (False == validate_args_fields(paitent_fields, request_arg)):
        response = app.response_class(
                    response="Bad request check field!",
                    status=400,
                    mimetype='application/text'
                )
        return response

    if request.method == 'POST':
        try:
            if (len(request_arg.keys()) == 0):
                raise HTTPError(url=request.url, code=400, msg="Bad Request!!", hdrs=request.headers, fp="")
            else:
                update_item = request_arg.copy()
                new_paitent = Patient(**update_item)
                db_session.add(new_paitent)
                db_session.commit()
                response = app.response_class(
                    response="SUCCESS!",
                    status=200,
                    mimetype='application/text'
                )
            return response
        except HTTPError as e:
            raise e

    if request.method == 'GET':
        result = ""
        try:
            if (len(request_arg.keys()) == 0):
                result = Patient.query.all()
                result = [r.to_dict() for r in result]
            else:
                result = db_session.query(Patient).filter_by(**request_arg).all()
                result = [r.to_dict() for r in result]
            response = app.response_class(
                        response=json.dumps(result),
                        status=200,
                        mimetype='application/json'
                    )
            return response
        except HTTPError as e:
            raise e

    if request.method == 'PUT':
        try:
            if (len(request_arg.keys()) == 0):
                raise HTTPError(url=request.url, code=400, msg="Bad Request!!", hdrs=request.headers, fp="")
            else:
                update_item = request_arg.copy()
                del update_item['id']
                result = Patient.query.filter_by(id=request_arg.get('id')).update(update_item)
                db_session.commit()
                response = app.response_class(
                        response="SUCESS!",
                        status=200,
                        mimetype='application/text'
                    )
                return response
        except HTTPError as e:
            raise e

    if request.method == 'DELETE':
        try:
            print(request.json)
            if not request.json or not 'id' in request.json:
                raise HTTPError(url=request.url, code=400, msg="Bad Request!!", hdrs=request.headers, fp="")
            else:
                result = Patient.query.filer_by(id=request.json.get('id')).delete()
                db_session.commit()
                return ("SUCESS!")
        except HTTPError as e:
            raise e

@app.route("/roles", methods=['GET', 'POST', 'PUT', 'DELETE'])
@cross_origin()
def roles():

    request_url = request.url
    request_arg = dict(request.args)
    paitent_fields = ['roles']

    if (False == validate_args_fields(paitent_fields, request_arg)):
        response = app.response_class(
                    response="Bad request check field!",
                    status=400,
                    mimetype='application/text'
                )
        return response

    if request.method == 'POST':
        try:
            if (len(request_arg.keys()) == 0):
                raise HTTPError(url=request.url, code=400, msg="Bad Request!!", hdrs="", fp="")
            else:
                update_item = request_arg.copy()
                new_roles = Roles(**update_item)
                db_session.add(new_roles)
                db_session.commit()
                response = app.response_class(
                    response="SUCCESS!",
                    status=200,
                    mimetype='application/text'
                )
            return response
        except HTTPError as e:
            raise e

    if request.method == 'GET':
        result = ""
        try:
            if (len(request_arg.keys()) == 0):
                result = Roles.query.all()
                result = [r.to_dict() for r in result]
            else:
                result = db_session.query(Roles).filter_by(**request_arg).all()
                result = [r.to_dict() for r in result]
            response = app.response_class(
                        response=json.dumps(result),
                        status=200,
                        mimetype='application/json'
                    )
            return response
        except HTTPError as e:
            raise e

    if request.method == 'PUT':
        try:
            if (len(request_arg.keys()) == 0):
                raise HTTPError(url=request.url, code=400, msg="Bad Request!!", hdrs=request.headers, fp="")
            else:
                update_item = request_arg.copy()
                del update_item['id']
                result = Roles.query.filter_by(id=request_arg.get('id')).update(update_item)
                db_session.commit()
                response = app.response_class(
                        response="SUCESS!",
                        status=200,
                        mimetype='application/text'
                    )
                return response
        except HTTPError as e:
            raise e

    if request.method == 'DELETE':
        try:
            print(request.json)
            if not request.json or not 'id' in request.json:
                raise HTTPError(url=request.url, code=400, msg="Bad Request!!", hdrs=request.headers, fp="")
            else:
                result = Roles.query.filer_by(id=request.json.get('id')).delete()
                db_session.commit()
                return ("SUCESS!")
        except HTTPError as e:
            raise e


@app.route("/users", methods=['GET', 'POST', 'PUT', 'DELETE'])
@cross_origin()
def users():

    request_url = request.url
    request_arg = dict(request.args)
    paitent_fields = ['user_name', 'passwd', 'role_id']

    if (False == validate_args_fields(paitent_fields, request_arg)):
        response = app.response_class(
                    response="Bad request check field!",
                    status=400,
                    mimetype='application/text'
                )
        return response

    if request.method == 'POST':
        try:
            if (len(request_arg.keys()) == 0):
                raise HTTPError(url=request.url, code=400, msg="Bad Request!!", hdrs="", fp="")
            else:
                update_item = request_arg.copy()
                new_user = User(**update_item)
                db_session.add(new_user)
                db_session.commit()
                response = app.response_class(
                    response="SUCCESS!",
                    status=200,
                    mimetype='application/text'
                )
            return response
        except HTTPError as e:
            raise e

    if request.method == 'GET':
        result = ""
        try:
            if (len(request_arg.keys()) == 0):
                result = User.query.all()
                result = [r.to_dict() for r in result]
            else:
                result = db_session.query(User).filter_by(**request_arg).all()
                result = [r.to_dict() for r in result]
            response = app.response_class(
                        response=json.dumps(result),
                        status=200,
                        mimetype='application/json'
                    )
            return response
        except HTTPError as e:
            raise e

    if request.method == 'PUT':
        try:
            if (len(request_arg.keys()) == 0):
                raise HTTPError(url=request.url, code=400, msg="Bad Request!!", hdrs=request.headers, fp="")
            else:
                update_item = request_arg.copy()
                del update_item['id']
                result = User.query.filter_by(id=request_arg.get('id')).update(update_item)
                db_session.commit()
                response = app.response_class(
                        response="SUCESS!",
                        status=200,
                        mimetype='application/text'
                    )
                return response
        except HTTPError as e:
            raise e

    if request.method == 'DELETE':
        try:
            print(request.json)
            if not request.json or not 'id' in request.json:
                raise HTTPError(url=request.url, code=400, msg="Bad Request!!", hdrs=request.headers, fp="")
            else:
                result = User.query.filer_by(id=request.json.get('id')).delete()
                db_session.commit()
                return ("SUCESS!")
        except HTTPError as e:
            raise e

@app.route("/login", methods=['POST'])
@cross_origin()
def login(client, username, password):

    try:
        return client.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)
    except:
        raise HTTPError(code=403, msg="Not welcomed here!")

@app.route("/login", methods=['POST'])
@cross_origin()
def logout(client):
    return client.get('/logout', follow_redirects=True)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='127.0.1.1', port='1990', use_reloader=True, use_debugger=True)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    import db.database
    database.init_db()