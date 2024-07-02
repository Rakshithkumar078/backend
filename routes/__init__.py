from flask import Blueprint
from .category_routes import category_bp

api_bp = Blueprint('api', __name__)
api_bp.register_blueprint(category_bp)