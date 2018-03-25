#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask,render_template
import os
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/')
def index():
    list = os.listdir('/home/shiyanlou/shiyanlou/flask/files')
    return render_template('index.html',list=list)
@app.route('/files/<filename>')
def file(filename):
    return render_template('file.html',filename=filename)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
