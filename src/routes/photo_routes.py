from flask import Blueprint, request, jsonify, session
from src.models.photo import Photo

photo_bp = Blueprint('photo_bp', __name__)

@photo_bp.route('/upload', methods=['POST'])
def upload_photo():
    if 'userid' not in session:
        return jsonify({"message": "인증 실패"}), 401

    data = request.get_json()
    uploader_id = session['userid']
    description = data['description']
    keywords = data['keywords']
    imageName = data['imageName']
    photo = Photo(uploader_id, description, keywords, imageName)
    photo.save()
    return jsonify({"message": "이미지 업로드 성공"}), 201

@photo_bp.route('/search', methods=['GET'])
def search_photos():
    keyword = request.args.get('keyword')
    photos = Photo.search_by_keyword(keyword)
    return jsonify(photos), 200

