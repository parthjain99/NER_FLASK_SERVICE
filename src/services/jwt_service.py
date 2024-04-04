from functools import wraps
import jwt
from flask import request, abort
from flask import current_app
from src.models.user_model import User as models
import logging

logger = logging.getLogger(__name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        logger.info("Verifying user authentication status")
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            logger.critical("Authentication Token is missing!")
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            if not data:
                logger.critical("Invalid Authentication token!")
                return {
                    "message": "Invalid Authentication token!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
            current_user = models.query.filter_by(id=data["id"]).first()
            if current_user is None:
                logger.critical("User could not be authenticated!")
                return {
                    "message": "Invalid Authentication token!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
        except Exception as e:
            logger.critical("User could not be authenticated!")
            return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        logger.info("User is authenticated!")
        return f(current_user, *args, **kwargs)

    return decorated
