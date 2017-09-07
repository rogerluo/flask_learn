from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import os
from datetime import datetime

class NameForm(Form):
    name = StringField("what is your name?", validators=[Required()])
    submit = SubmitField('Submit')



# from flask_bootstrap import BootStrap
app = Flask(__name__)
# app.jinja_env.trim_blocks = True  
# app.jinja_env.lstrip_blocks = True  
app.config['SECRET_KEY'] = 'hard to guess string' # must set, or error 'A secret key is required to use CSRF'
bootstrap = Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] =\
'mysql://root:root1234@127.0.0.1/test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column('Fid', db.Integer, primary_key=True)
    name = db.Column('Fuser', db.String(32), unique=True, index=True)
    modifytime = db.Column('Fmodify_time', db.DateTime, index=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user is None:
            user = User(name = form.name.data, modifytime = datetime.now())
            db.session.add(user)
            session['known'] = False 
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for("index"))
    return render_template('db_index.html', form=form, name=session.get('name'),
        known = session.get('known', False))

@app.route('/user/<name>')
def user2(name):
    return render_template('user_bootstrap.html', name=name)



    def __repr__(self):
        return "<User %r>" % (self.name)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)