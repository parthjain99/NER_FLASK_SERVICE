from flask import Blueprint
from src.controllers.user_controller import users
from src.controllers.NER_controller import ner
from src.controllers.auth_controller import auth
# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(users, url_prefix="/users")
api.register_blueprint(ner, url_prefix="/ner")
api.register_blueprint(auth, url_prefix="/auth")