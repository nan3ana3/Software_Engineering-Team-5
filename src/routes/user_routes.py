from flask import Blueprint, request, jsonify, session, render_template
from src.models.user import User

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@user_bp.route('/signup', methods=['POST'])
def sign_up():
    data = request.get_json()
    username = data['username']
    userid = data['userid']
    password = data['password']
    user = User(username, userid, password)
    user.save()
    return jsonify({"message": "유저 생성"}), 201


@user_bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    userid = data['userid']
    password = data['password']
    user = User.login(userid, password)
    if user:
        session['userid'] = userid
        return jsonify({"message": "로그인 성공"}), 200
    return jsonify({"message": "로그인 실패"}), 401

@user_bp.route('/signout', methods=['POST'])
def sign_out():
    session.pop('userid', None)
    return jsonify({"message": "로그아웃 성공"}), 200

@user_bp.route('/list', methods=['GET'])
def get_user_list():
    users = User.get_user_list()
    return jsonify(users), 200
