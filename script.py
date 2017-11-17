from flask import Flask, render_template
from flask import request
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')