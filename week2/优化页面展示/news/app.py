#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask,render_template,abort
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from datetime import datetime
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/shiyanlou'
client = MongoClient('127.0.0.1',27017)
nsdb = client.shiyanlou
db = SQLAlchemy(app)
class File(db.Model):
    __tablename__= 'file'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category')
    content = db.Column(db.Text)
    def add_tag(self,tag_name):
        id_tag = nsdb.user.find_one({'file_id':self.id})
        if id_tag:
            tag = id_tag['tags']
            tag.append(tag_name)
            nsdb.user.update_one({'file_id':self.id},{'$set':{'tags':tag}})
            return tag
        else:
            tag = [tag_name]
            nsdb.user.insert_one({'file_id':self.id,'tags':tag})
        return tag
    def remove_tag(self,tag_name):
        id_tag = nsdb.user.find_one({'file_id':self.id})
        tag = id_tag['tags']
        tag.remove(tag_name)
        nsdb.user.update_one({'file_id':self.id},{'$set':{'tags':tag}})
        return tag
    @property
    def tags(self):
        id_tag = nsdb.user.find_one({'file_id':self.id})
        if id_tag:
            return id_tag['tags']
        else:
            return []
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
    list = db.session.query(File).all()
    return render_template('index.html',list=list)
@app.route('/files/<int:file_id>')
def file(file_id):
    files = File.query.get_or_404(file_id)
    title = db.session.query(File.title).filter(File.id==file_id).all()
    content = db.session.query(File.content).filter(File.id==file_id).all()
    category = db.session.query(Category.name).filter(Category.id ==file_id).all()
    created_time = db.session.query(File.created_time).filter(File.id==file_id).all()
    return render_template('file.html',title=title,content=content,created_time=created_time,category=category)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
