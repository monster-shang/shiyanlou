#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask,render_template,abort
from flask_sqlalchemy import SQLAlchemy
import os,json
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)
class File(db.Model):
    __tablename__= 'file'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    categoty = db.relationship('category')
    content = db.Column(db.Text)
    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content
    def __repr__(self):
        return "<File(name=%s)>" % self.category_id
class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key = True,)
    name = db.Column(db.String(80))
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return "<Category(name=%s)>" % self.name 
@app.route('/')
def index():
    list = os.listdir('/home/shiyanlou/shiyanlou/flask/files')
    return render_template('index.html',list=list)
@app.route('/files/<filename>')
def file(filename):
    if not os.path.exists('/home/shiyanlou/shiyanlou/flask/files/'+filename+'.json'):
        abort(404)
    with open('/home/shiyanlou/shiyanlou/flask/files/'+filename+'.json','r') as file:
        txt = json.loads(file.read())
    title = txt['title']
    content = txt['content']
    created_time = txt['created_time']
    return render_template('file.html',filename=filename,title=title,content=content,created_time=created_time)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
