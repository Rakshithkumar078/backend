from . import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    result = db.Column(db.String(100), nullable=False, unique=True)
    teststeps = db.Column(db.String(255), nullable=False, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'result': self.result,
            'teststeps': self.teststeps
        }