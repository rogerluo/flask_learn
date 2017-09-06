from flask import Flask, render_template
from flask_bootstrap import Bootstrap
# from flask_bootstrap import BootStrap
app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/user/<name>')
def user(name):
    return render_template('user_bootstrap.html', name=name)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)