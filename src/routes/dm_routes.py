from flask import Blueprint, request, jsonify, session
from src.models.dm import DM

dm_bp = Blueprint('dm_bp', __name__)

@dm_bp.route('/send', methods=['POST'])
def send_message():
    if 'userid' not in session:
        return jsonify({"message": "Unauthorized"}), 401

    data = request.get_json()
    sender_id = session['userid']
    receiver_id = data['receiver_id']
    content = data['content']
    parent_mid = data.get('parent_mid')
    dm = DM(sender_id, receiver_id, content, parent_mid)
    dm.save()
    return jsonify({"message": "메시지 송신"}), 201

@dm_bp.route('/list', methods=['GET'])
def get_messages():
    if 'userid' not in session:
        return jsonify({"message": "권한 없음"}), 401

    user_id = session['userid']
    messages = DM.get_messages(user_id)
    return jsonify(messages), 200

@dm_bp.route('/delete/<mid>', methods=['DELETE'])
def delete_message(mid):
    if 'userid' not in session:
        return jsonify({"message": "권한 없음"}), 401

    DM.delete_message(mid)
    return jsonify({"message": "메시지 삭제 성공"}), 200
