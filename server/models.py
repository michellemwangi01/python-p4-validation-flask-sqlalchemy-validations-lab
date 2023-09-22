from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint

db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

    @validates('phone_number')
    def check_phone_number(self,key, address):
        if len(address) != 10:
            raise ValueError("Enter a valid phone number")

    @validates('name')
    def check_name(self, key, address):
        if address == '':
            raise ValueError("Enter a valid name")




class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'

    @validates('content')
    def checks_content(self, key, address):
        if len(address)<250:
            raise ValueError("Content too short test. Less than 250 chars.")

    @validates('summary')
    def checks_content(self, key, address):
        if len(address) > 250:
            raise ValueError("Summary too long test. More than 250 chars.")

    @validates('category')
    def checks_content(self, key, address):
        if address in ['Fiction', 'Non-Fiction']:
            raise ValueError("Summary too long test. More than 250 chars.")
