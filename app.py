from flask import Flask, render_template, redirect, url_for, request, abort, flash
from flask_bootstrap import Bootstrap5
import forms

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
)

bootstrap = Bootstrap5(app)

@app.route('/')
def index():
    return redirect(url_for('feed'))

@app.route('/feed/', methods=['GET', 'POST'])
def feed():
    return render_template('feed.html') 
   

@app.route('/profile/<int:id>', methods=['GET', 'POST'])
def profile(id):
    return 'profile-detail'
   
      
   

