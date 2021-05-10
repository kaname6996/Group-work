#$env:FLASK_APP="app.py" 執行flask
from flask import Flask , request,abort,session;
from flask import render_template,make_response;
from flask import redirect,url_for;
import numpy as np;
import cv2;
from werkzeug.utils import secure_filename;
import os;
import time;



app = Flask(__name__,static_folder="media")
@app.route('/',methods =['post','get']) 
def index(): 
	if request.method =='POST':
		if request.values['send']=='送出':
			return render_template('AAAA.html',name=request.values['user'])
	return render_template('AAAA.html',name="")


@app.route('/客服專區.html',methods =['post','get']) 
def dk4zj6(): 
	return render_template('客服專區.html')

@app.route('/index.html',methods =['post','get']) 
def g3u(): 
	return render_template('AAAA.html')