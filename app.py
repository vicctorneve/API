from flask import Flask
from routes.clientes_routes import cliente_bp
from config.config import Config
from models.cliente import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(cliente_bp)


if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)