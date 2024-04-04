from flask import request, Response, json, Blueprint
from src import bcrypt, db
from datetime import datetime
import jwt
import os
import logging
from src.models.user_model import TextData, NamedEntity, User
from src.services.NER_service import ner_spacy
from src.services.jwt_service import token_required
from uuid import uuid4

# user controller blueprint to be registered with api blueprint
ner = Blueprint("ner", __name__)
logger = logging.getLogger(__name__)

@ner.route('/ner_post', methods = ["POST"])
@token_required
def handle_ner_post(current_user,*args, **kwargs):
    try: 
        # first check user parameters
        data = request.json
        if "text" in data:
            # check db for user records
            text_id = str(uuid4())
            text_obj = TextData(
                user_id = current_user.id,
                text_id = text_id,
                text_content = data["text"],
                submitted_at = datetime.utcnow(),
            )
            db.session.add(text_obj)
            db.session.commit()
        logger.info("Text added to text model")
    except Exception as e:
        logger.critical(f"Cannot add to text model: {str(e)}")
        return Response(
            response=json.dumps({'status': "failed", "message": "Internal Server Error"}),
            status=500,
            mimetype='application/json'
            )
    try:
        ner_obj = ner_spacy(data["text"])
        for entity_key,entity in ner_obj.items():
            entity_obj = NamedEntity(
                text_id = text_id,
                entity_id = str(uuid4()),
                entity_type = entity['label'],
                entity_value = entity['text'],
                entity_start = entity['start_char'],
                entity_end = entity['end_char']
            )
            db.session.add(entity_obj)
        db.session.commit()
        logger.info("NER successful")
        return Response(
            response=json.dumps({'status': "success",
                                "message": "NER Successful",
                                "entities": ner_obj,
                                "text_id": text_id}),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        logger.critical(f"Cannot commit or generate ner: {str(e)}")
        return Response(
            response=json.dumps({'status': "failed", "message": "Internal Server Error"}),
            status=500,
            mimetype='application/json'
        )
    

@ner.route('/ner_get', methods = ["GET"])
@token_required
def handle_ner_get(current_user, *args, **kwargs):
    try:
        data = request.json
        if data:
            entities = NamedEntity.query.filter_by(text_id = data['text_id']).all()
            text = TextData.query.filter_by(text_id = data['text_id']).first()
            if not entities:
                return Response(
                    response=json.dumps({'status': "failed", "message": "No entities found"}),
                    status=404,
                    mimetype='application/json'
                )
            if text.user_id != current_user.id and current_user.role != "admin":
                return Response(
                    response=json.dumps({'status': "failed", "message": "Unauthorized"}),
                    status=401,
                    mimetype='application/json'
                )
            entities_list = []
            for entity in entities:
                entity_dict = {
                    "entity_id": entity.entity_id,
                    "entity_type": entity.entity_type,
                    "entity_value": entity.entity_value,
                    "entity_start": entity.entity_start,
                    "entity_end": entity.entity_end
                }
                entities_list.append(entity_dict)
            logger.info("Entities fetched successfully")
            return Response(
                response=json.dumps({'status': "success",
                                    "message": "NER Successful",
                                    "text": text.text_content,
                                    "entities": entities_list}),
                status=200,
                mimetype='application/json'
            )
        else:
            logger.critical("text_id is required")
            return Response(
                response=json.dumps({'status': "failed", "message": "text_id is required"}),
                status=400,
                mimetype='application/json'
            )
    except Exception as e:
        logger.error(f"Cannot get entities: {str(e)}")
        return Response(
            response=json.dumps({'status': "failed", "message": "Internal Server Error"}),
            status=500,
            mimetype='application/json'
        )


@ner.route('/ner_delete', methods = ["DELETE"])
@token_required
def handle_ner_delete(current_user,*args, **kwargs):
    try:
        data = request.json
        if 'text_id' in data:
            entities = NamedEntity.query.filter_by(text_id = data['text_id']).all()
            textdata = TextData.query.filter_by(text_id = data['text_id']).first()
            if not entities:
                return Response(
                    response=json.dumps({'status': "failed", "message": "No entities found"}),
                    status=404,
                    mimetype='application/json'
                )
            if textdata.user_id != current_user.id and current_user.role != "admin":
                return Response(
                    response=json.dumps({'status': "failed", "message": "Unauthorized"}),
                    status=401,
                    mimetype='application/json'
                )
            for entity in entities:
                db.session.delete(entity)
            db.session.commit()
            db.session.delete(textdata)
            db.session.commit()
            logger.info("NER Delete successful")
            return Response(
                response=json.dumps({'status': "success",
                                    "message": "NER Delete successful"}),
                status=200,
                mimetype='application/json'
            )
        else:
            logger.critical("text_id is required")
            return Response(
                response=json.dumps({'status': "failed", "message": "text_id is required"}),
                status=400,
                mimetype='application/json'
            )
    except Exception as e:
        logger.exception(f"Cannot delete entities: {str(e)}")
        return Response(
            response=json.dumps({'status': "failed", "message": "Internal Server Error"}),
            status=500,
            mimetype='application/json'
        )

