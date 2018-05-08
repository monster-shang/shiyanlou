from flask import Blueprint, render_template
from simpledu.models import Course

admin = Blueprint('admin', __name__,url_prefix='/admin')

@admin.route('/')
def index():
    return 'admin'
