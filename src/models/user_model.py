from src import db

class User(db.Model):
    id = db.Column(db.String(100), primary_key = True)
    firstname = db.Column(db.String(60), nullable=False)
    lastname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(255), unique = True, nullable=False)
    role = db.Column(db.Enum('admin', 'user', name='roles'), default='user')
    password =  db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default='CURRENT_db.TIMESTAMP')

class TextData(db.Model):
    text_id = db.Column(db.Text, primary_key=True, unique=True)
    user_id = db.Column(db.Text, db.ForeignKey('user.id'))
    text_content = db.Column(db.Text, nullable=False)
    submitted_at = db.Column(db.TIMESTAMP, nullable=False, server_default='CURRENT_db.TIMESTAMP')

class NamedEntity(db.Model):
    entity_id = db.Column(db.Text, nullable=False, primary_key=True)
    text_id = db.Column(db.Text, db.ForeignKey('text_data.text_id'), primary_key = True)
    entity_type = db.Column(db.Text, nullable=False)
    entity_value = db.Column(db.String(255), nullable=False)
    entity_end = db.Column(db.Integer, nullable=False)
    entity_start = db.Column(db.Integer, nullable=False)
