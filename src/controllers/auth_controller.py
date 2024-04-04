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
auth = Blueprint("auth", __name__)
logger = logging.getLogger(__name__)

# route for login api/users/signin
@auth.route('/signin', methods = ["POST"])
def handle_login():
    try: 
        # first check user parameters
        data = request.json
        if "email" and "password" in data:
            # check db for user records
            user = User.query.filter_by(email = data["email"]).first()

            # if user records exists we will check user password
            if user:
                # check user password
                if bcrypt.check_password_hash(user.password, data["password"]):
                    # user password matched, we will generate token
                    payload = {
                        'created_at': datetime.utcnow().isoformat(),
                        'id': str(user.id).replace('-',"-"),
                        'firstname': user.firstname,
                        'lastname': user.lastname,
                        'email': user.email,
                    }
                    token = jwt.encode(payload = payload,key = os.getenv('SECRET_KEY'),algorithm='HS256')
                    logger.info("User Sign In Successful")
                    return Response(
                            response=json.dumps({'status': "success",
                                                "message": "User Sign In Successful",
                                                "token": token}),
                            status=200,
                            mimetype='application/json'
                        )
                
                else:
                    logger.critical("User Password Mistmatched")
                    return Response(
                        response=json.dumps({'status': "failed", "message": "User Password Mistmatched"}),
                        status=401,
                        mimetype='application/json'
                    ) 
            # if there is no user record
            else:
                logger.info("User Record doesn't exist")
                return Response(
                    response=json.dumps({'status': "failed", "message": "User Record doesn't exist, kindly register"}),
                    status=404,
                    mimetype='application/json'
                ) 
        else:
            # if request parameters are not correct 
            logger.critical("User Parameters Email and Password are required")
            return Response(
                response=json.dumps({'status': "failed", "message": "User Parameters Email and Password are required"}),
                status=400,
                mimetype='application/json'
            )
        
    except Exception as e:
        logger.critical("sign in failed")
        return Response(
                response=json.dumps({'status': "failed", 
                                     "message": "Error Occured",
                                     "error": str(e)}),
                status=500,
                mimetype='application/json'
            )

# route for login api/users/signup
@auth.route('/signup', methods = ["POST"])
def handle_signup():
    try: 
        # first validate required use parameters
        data = request.json
        if "firstname" in data and "lastname" and data and "email" and "password" in data:
            # validate if the user exist 
            user = User.query.filter_by(email = data["email"]).first()
            # usecase if the user doesn't exists
            user_id = str(uuid4())
            if not user:
                # creating the user instance of User Model to be stored in DB
                user_obj = User(
                    firstname = data["firstname"],
                    lastname = data["lastname"],
                    email = data["email"],
                    # hashing the password
                    password = bcrypt.generate_password_hash(data['password']).decode('utf-8'),
                    created_at =  datetime.utcnow(),
                    id = user_id
                )
                db.session.add(user_obj)
                db.session.commit()

                # lets generate jwt token
                payload = {
                    'created_at': datetime.utcnow().isoformat(),
                    'id': str(user_id),
                    'firstname': user_obj.firstname,
                    'lastname': user_obj.lastname,
                    'email': user_obj.email,
                }
                token = jwt.encode(payload = payload,key = os.getenv("SECRET_KEY"),algorithm="HS256")
                logger.info("User Sign up Successful")
                return Response(
                response=json.dumps({'status': "success",
                                    "message": "User Sign up Successful",
                                    "token": token}),
                status=201,
                mimetype='application/json'
            )
            else:
                logger.info("User already exists")
                # if user already exists
                return Response(
                response=json.dumps({'status': "failed", "message": "User already exists kindly use sign in"}),
                status=409,
                mimetype='application/json'
            )
        else:
            # if request parameters are not correct 
            logger.critical("User Parameters Firstname, Lastname, Email and Password are not present")
            return Response(
                response=json.dumps({'status': "failed", "message": "User Parameters Firstname, Lastname, Email and Password are required"}),
                status=400,
                mimetype='application/json'
            )
        
    except Exception as e:
        logger.critical("sign up failed")
        return Response(
                response=json.dumps({'status': "failed", 
                                     "message": "Error Occured",
                                     "error": str(e)}),
                status=500,
                mimetype='application/json'
            )
