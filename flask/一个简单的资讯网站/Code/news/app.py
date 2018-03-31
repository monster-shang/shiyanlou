#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask,render_template,abort
import os,json
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/')
def index():
    list = os.listdir('/home/shiyanlou/files')
    return render_template('index.html',list=list)
@app.route('/files/<filename>')
def file(filename):
    if not os.path.exists('/home/shiyanlou/files/'+filename+'.json'):
        abort(404)
    with open('/home/shiyanlou/files/'+filename+'.json','r') as file:
        txt = json.loads(file.read())
    title = txt['title']
    content = txt['content']
    created_time = txt['created_time']
    return render_template('file.html',filename=filename,title=title,content=content,created_time=created_time)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
