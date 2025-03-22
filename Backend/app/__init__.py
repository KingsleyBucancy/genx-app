from flask import Flask
from flask_cors import CORS
from app.config import Config


from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    from app.routes.transcribe import transcribe_bp
    app.register_blueprint(transcribe_bp)

    from app.routes.generate_code import codegen_bp
    app.register_blueprint(codegen_bp)


    return app
