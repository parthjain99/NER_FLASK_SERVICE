from flask import request, Response, json, Blueprint, jsonify, session
from src.models.user_model import User
from src import bcrypt, db
from datetime import datetime
import jwt
import os
import logging
from src.services.jwt_service import token_required
from src.models.user_model import User
from uuid import uuid4
# user controller blueprint to be registered with api blueprint
users = Blueprint("users", __name__)
logger = logging.getLogger(__name__)
# route for login api/users/signin

@users.route("/get_user", methods=["GET"])
@token_required
def get_current_user(user):
    try:
        user_data = {
                "id": user.id,
                "firstname": user.firstname,
                "lastname": user.lastname,
                "email": user.email,
                "created_at": user.created_at,
                "role": user.role
            }
        logger.info("User data fetched successfully")
        return jsonify({
            "data": user_data
        })
    except Exception as e:
        logger.critical("Error occurred while fetching user data")
        return Response(
            response=json.dumps({'status': "failed", 
                                    "message": "Error Occurred",
                                    "error": str(e)}),
            status=500,
            mimetype='application/json'
        )


@users.route("/update_user", methods=["PUT"])
@token_required
def update_user(current_user):
    try:
        user = request.json
        if user.get("firstname"):
            User.query.filter_by(id=current_user.id).update({
                "firstname": user["firstname"]
            })
            db.session.commit()
            logger.info("User data updated successfully")
            return jsonify({
                "message": "successfully updated account",
                "data": user
            }), 201
        if user.get("lastname"):
            User.query.filter_by(id=current_user.id).update({
                "lastname": user["lastname"]
            })     
            db.session.commit()       
            logger.info("User data updated successfully")
            return jsonify({
                "message": "successfully updated account",
                "data": user
            }), 201
        logger.critical("Invalid data, you can only update your account name!")
        return {
            "message": "Invalid data, you can only update your account name!",
            "data": None,
            "error": "Bad Request"
        }, 400
    except Exception as e:
        logger.critical("Error occurred while updating user data")
        return jsonify({
            "message": "failed to update account",
            "error": str(e),
            "data": None
        }), 400
    

@users.route("/delete_user", methods=["DELETE"])
@token_required
def disable_user(current_user):
    if current_user.role != "admin":
        logger.critical("User is not authorized to perform this action")
        return jsonify({
            "message": "You are not authorized to perform this action",
            "data": None
        }), 403
    user = request.json
    try:
        to_del_user = User.query.filter_by(email=user['email']).first()
        db.session.delete(to_del_user)
        db.session.commit()
        logger.info("User account disabled successfully")
        return jsonify({
            "message": "successfully disabled acount",
            "data": None
        }), 204
    except Exception as e:
        logger.critical("Error occurred while disabling user account")
        return jsonify({
            "message": "failed to disable account",
            "error": str(e),
            "data": None
        }), 400