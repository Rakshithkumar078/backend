from flask import Blueprint, request, jsonify
from services.category_service import get_all, get_by_id, add, update, delete

category_bp = Blueprint('categories', __name__, url_prefix='/categories')

@category_bp.route('/', methods=['GET'])
def get_all_categories():
    categories = get_all()
    return jsonify([category.to_dict() for category in categories])

@category_bp.route('/<int:id>/', methods=['GET'])
def get_categor_by_id(id):
    catgeory = get_by_id(id)
    if catgeory:
        return jsonify(catgeory.to_dict())
    return jsonify({'Error': f'Catgeory not found for id = {id}'}), 404

@category_bp.route('/', methods=['POST'])
def add_category():
    data = request.get_json()
    category = add(data['name'], data['result'], data['teststeps'])
    return jsonify(category.to_dict()), 201

@category_bp.route('/<int:id>/', methods=['PUT'])
def update_category(id):
    data = request.get_json()
    category = update(id, data['name'], data['result'], data['teststeps'])
    if category:
        return jsonify(category.to_dict())
    return jsonify({'Error': f'Category not found for id = {id}'}), 404

@category_bp.route('/<int:id>/', methods=['DELETE'])
def delete_category(id):
    category = delete(id)
    if category:
        return jsonify(category.to_dict())
    return jsonify({'Error': f'Category not found for id  = {id}'}), 404