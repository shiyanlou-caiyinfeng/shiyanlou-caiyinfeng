#!/usr/bin/env python3
import os
import json
from flask import Flask,render_template,abort

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

JSON_DIR_PATH='/home/shiyanlou/files'
class Config(object):
    def __init__(self):
        self._config=self.set_config()
    def set_config(self):
        result={}
        filenames=os.listdir(JSON_DIR_PATH)
        for filename1 in filenames:
            with open(os.path.join(JSON_DIR_PATH,filename1)) as file:
                filename=filename1.split('.')[0]
                result[filename]=json.loads(file.read())
        return result
    def get_title_config(self):
        titles={}
        for name,item in self._config.items():
            titles[name]=item.get('title')
        return titles
    def get_json_config(self,filename):
        return self._config.get(filename)
test=Config()
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
@app.route('/')
def index():
    return render_template('index.html',titles=test.get_title_config())
@app.route('/files/<filename>')
def file(filename):
    news=test.get_json_config(filename)
    if not filename:
        abort(404)
    return render_template('file.html',news=news)
if __name__=="__main__":
    app.run()
