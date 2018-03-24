from flask import Flask,render_template
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/files/<filename>')
def file(filename):
    return render_template('file.html')
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
