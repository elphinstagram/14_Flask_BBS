from main import db
from main import Article
from main import app

with app.app_context():
    # DB Create
    db.create_all()

    # Create Sample Data
    sample = Article(username="花子", email="hanako@me.com", post="ダイエットについて質問です")

    # Insert Sample Data
    db.session.add(sample)
    db.session.commit()

    # show data
    print(Article.query.all())

