from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField("what is your name?", validators=[Required()])
    submit = SubmitField('Submit')

# from flask_bootstrap import BootStrap
app = Flask(__name__)
# app.jinja_env.trim_blocks = True  
# app.jinja_env.lstrip_blocks = True  
app.config['SECRET_KEY'] = 'hard to guess string' # must set, or error 'A secret key is required to use CSRF'
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session['name'] 
        if (old_name is not None and old_name != form.name.data):
            flash('Looks like you change your name!')
        session['name'] = form.name.data
        return redirect(url_for("index"))
    return render_template('form_index.html', form=form, name=session.get('name'))
@app.route('/user/<name>')
def user(name):
    return render_template('user_bootstrap.html', name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)