from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from routes import api_bp
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# cors = CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]}})

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(debug=True)