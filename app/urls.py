# urls.py
from app.views import verify, processing_message
from app.decorators.security import signature_required
from flask import Blueprint

webhook_blueprint = Blueprint("webhook", __name__)

@webhook_blueprint.route("/webhook", methods=["GET"])
def webhook_get():
    return verify()

@webhook_blueprint.route("/webhook", methods=["POST"])
@signature_required
def webhook_post():
    return processing_message()
