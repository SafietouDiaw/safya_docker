from flask import request, abort
from models import db, Person, person_schema, persons_schema

def read_all():
    persons = Person.query.all()
    return persons_schema.dump(persons)

def create():
    data = request.get_json()
    new_person = person_schema.load(data)
    db.session.add(new_person)
    db.session.commit()
    return person_schema.dump(new_person), 201

def update(id):
    data = request.get_json()
    person = Person.query.get(id)
    if not person:
        abort(404, "Personne introuvable")

    person.nom = data.get("nom", person.nom)
    person.prenom = data.get("prenom", person.prenom)
    person.age = data.get("age", person.age)

    db.session.commit()
    return person_schema.dump(person)

def delete(id):
    person = Person.query.get(id)
    if not person:
        abort(404, "Personne introuvable")

    db.session.delete(person)
    db.session.commit()
    return {"message": "Personne supprimée"}, 200
