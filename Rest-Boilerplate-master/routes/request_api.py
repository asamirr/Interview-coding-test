"""The Endpoints to manage bids"""
import uuid
from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint
from model import model as mod
from validate_email import validate_email
import json

REQUEST_API = Blueprint('request_api', __name__)

def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API

@REQUEST_API.route('/request', methods=['GET'])
def get_bids():
    """Return all bids
    @return: 200: an array of all known bids as a \
    flask/response object with application/json mimetype.
    """
    all_bids = mod.list_bids()
    return jsonify(all_bids)

@REQUEST_API.route('/request', methods=['POST'])
def place_bid():
    """Place a bid on a pet
    @param userID: post : User's ID
    @param amount: post : Amount of money for the bid
        @param petID: post : Pet's ID
    @return: 201: a new_uuid as a flask/response object \
    with application/json mimetype.
    @raise 400: misunderstood request
    """
    if not request.get_json():
        abort(400)
    data = request.get_json(force=True)

    if not data.get('userID'):
        abort(400)
    if not data.get('amount'):
        abort(400)
    if not data.get('petID'):
        abort(400)

    #new_uuid = str(uuid.uuid4())
    mod.place_a_bid(data['petID'], data['amount'], data['userID'])
    # HTTP 200 Created
    # return jsonify({"id": new_uuid}), 200
    resp = {"status": "OK"}
    return jsonify(resp)