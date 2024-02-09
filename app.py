from flask import Flask,render_template,request
import pandas as pd 
import re 

app =Flask(__name__)
@app.route('/')
def preliminary():
    return render_template('preliminary.html')

if __name__ == '__main__':
    app.run(debug=True,port=9700)