from flask import Flask, render_template

from models import db, Owner, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    owners = Owner.query.all()
    return render_template('index.html', owners=owners)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
