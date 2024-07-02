from models.category import Category
from models import db

def get_all():
    categories = Category.query.all()
    return categories

def get_by_id(id):
    return Category.query.get(id)

def add(name, result, teststeps):
    catgeory = Category(name=name, result=result, teststeps=teststeps)
    db.session.add(catgeory)
    db.session.commit()
    return catgeory

def update(id, name, result, teststeps):
    catgeory = Category.query.get(id)
    if catgeory:
        catgeory.name = name
        catgeory.result = result
        catgeory.teststeps = teststeps
        db.session.commit()
        return catgeory
    return None

def delete(id):
    catgeory = Category.query.get(id)
    if catgeory:
        db.session.delete(catgeory)
        db.session.commit()
        return catgeory
    return None