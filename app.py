from flask import Flask, render_template, redirect, url_for, request, abort, flash
from flask_bootstrap import Bootstrap5
import forms

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
)

from db import db, ProfessorProfile
from forms import ProfSearchForm

bootstrap = Bootstrap5(app)

@app.route('/')
def index():
    return redirect(url_for('feed'))

@app.route('/feed/', methods=['GET', 'POST'])
def feed():
    form = forms.ProfSearchForm()
    professors = db.session.execute(db.select(ProfessorProfile)).scalars().all()
    if request.method == 'POST' and form.validate():
        duchbegriff = form.search.data.lower()
    
    professors =[ prof for prof in professors
                    if suchbegriff in f"{prof.user.first_name} {prof.user.last_name}".lower()
                    or (prof.research_areas and suchbegriff in prof.research_areas.lower())]
    return render_template('feed.html', form=form, professoren=professors)
    

@app.route('/profile/<int:id>', methods=['GET', 'POST'])
def profile(id):
    prof = db.session.get(ProfessorProfile, id)
    return render_template('profile-detail.html', prof=prof)
