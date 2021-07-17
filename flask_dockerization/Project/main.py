from flask import Blueprint

main_bp = Blueprint("main_bp", __name__)

@main_bp.get('/')
def index():
    return {
        "msg": "Hello World"
    }