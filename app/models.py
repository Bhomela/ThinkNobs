from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique= False, index = True)
    email = db.Column(db.String(32), unique = False, index = True)
    phone_number = db.Column(db.Integer, index= True, unique = False)
    message = db.Column(db.Text)

    def __repr__(self):
        return '<User %r>' % self.name
