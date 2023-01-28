from flask import Flask, render_template, request
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

@app.route("/", methods=["GET","POST"])
def bbs():

    if request.method == "POST":
        # Create Sample Data
        username = request.form["name"]
        email = request.form["email"]
        post = request.form["message"]

        article = Article(username=username, email=email, post=post)

        # Insert Article Data to DB
        db.session.add(article)
        db.session.commit()

    title = "Flaskで作る掲示板"
    articles = Article.query.all()
    return render_template("index.html", title=title, articles=articles)

if __name__ == "__main__":
    app.run(debug=True)