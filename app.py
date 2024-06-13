from src.routes.dm_routes import dm_bp
from src.routes.photo_routes import photo_bp
from src.routes.user_routes import user_bp
from src.models.db import init_db
from flask import Flask, render_template, send_from_directory
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = Flask(__name__)

init_db(app)

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(photo_bp, url_prefix='/photos')
app.register_blueprint(dm_bp, url_prefix='/dms')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')


@app.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')


@app.route('/main', methods=['GET'])
def mainLoggedin_page():
    return render_template('main-loged-in.html')


@app.route('/receivedDM', methods=['GET'])
def receivedDM_page():
    return render_template('recieved-d-m.html')


@app.route('/sendedDM', methods=['GET'])
def sendedDM_page():
    return render_template('sended-d-m.html')


@app.route('/sendingDM', methods=['GET'])
def sendingDM_page():
    return render_template('sending-d-m.html')


@app.route('/modifyme', methods=['GET'])
def modifyme_page():
    return render_template('modify-me.html')


@app.route('/mypage', methods=['GET'])
def mypage_page():
    return render_template('my-page.html')


@app.route('/uploadpost', methods=['GET'])
def uploadpost_page():
    return render_template('upload-post.html')


@app.route('/mypost', methods=['GET'])
def mypost():
    return render_template('my-post.html')


@app.route('/otherpost', methods=['GET'])
def otherpost():
    return render_template('otherpost.html')


if __name__ == '__main__':
    app.run(debug=True)
