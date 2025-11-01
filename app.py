from flask import Flask

from routes.homepage import homepage_bp
from routes.login import login_bp
from routes.cadastro import cadastro_bp
from routes.picking import picking_bp
from routes.upload import upload_bp
from routes.caminhoes import caminhoes_bp



app = Flask(__name__)
app.secret_key = "secret_key"

# REGISTRAR BLUEPRINTS
app.register_blueprint(homepage_bp)
app.register_blueprint(login_bp)
app.register_blueprint(cadastro_bp)
app.register_blueprint(picking_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(caminhoes_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)