#!/usr/bin/env python3
import os
import json
from flask import Flask,render_template,abort

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

JSON_DIR_PATH='/home/shiyanlou/files'
class Config(object):
    def __init__(self):
        self._config={}
    def set_config(self,filename):
        with open(os.path.join(JSON_DIR_PATH,filename)) as file:
            self._config=json.loads(file.read())
    def get_config(self,value):
        return self._config[value]
    def get_json_config(self):
        return self._config
test=Config()
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
@app.route('/')
def index():
    return render_template('index.html',)
@app.route('/files/<filename>')
def file(filename):
    test.set_connfig(filename)
    news=get_json_config
    if not filename:
        abort(404)
    return render_template('file.html',news=news)
if __name__=="__main__":
    app.run()
