import sys
import os
print(sys.path)

'''
import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session

#from flask_session import Session
#from tempfile import mkdtemp
#rom werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
#mport sys

app = Flask(__name__)



#app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('template/index.html')
def displaying_home_page():
    return render_template('index.html')
if name == '__main__':
    app.run()
'''


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()




