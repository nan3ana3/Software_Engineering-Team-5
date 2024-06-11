import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from flask import Flask, render_template, send_from_directory
from src.models.db import init_db
from src.routes.user_routes import user_bp
from src.routes.photo_routes import photo_bp
from src.routes.dm_routes import dm_bp

app = Flask(__name__)

init_db(app)

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(photo_bp, url_prefix='/photos')
app.register_blueprint(dm_bp, url_prefix='/dms')


if __name__ == '__main__':
    app.run(debug=True)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'