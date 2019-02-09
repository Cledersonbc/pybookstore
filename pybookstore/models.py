from pybookstore import db


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(1000), nullable=False)
    author = db.Column(db.String(64), nullable=False)
    publisher = db.Column(db.String(64), nullable=True)
    edition = db.Column(db.Integer, nullable=True)
    isbn = db.Column(db.String(13), nullable=True, unique=True)
    format = db.Column(db.String(32), nullable=True)
    language = db.Column(db.String(32), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Numeric(precision=2), nullable=True)
    height = db.Column(db.Numeric(precision=1), nullable=True)
    width = db.Column(db.Numeric(precision=1), nullable=True)
    pages = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Numeric(precision=2), nullable=True)

    def __repr__(self):
        return "<Book(id='%s', title='%s', author='%s')>" % (
            self.id, self.title, self.author)
