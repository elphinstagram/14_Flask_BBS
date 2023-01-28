from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    post = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def bbs():
    title = "Flaskで作る掲示板"
    return render_template("index.html", title=title)

if __name__ == "__main__":
    app.run(debug=True)