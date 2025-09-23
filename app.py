from flask import Flask

from routes.homepage import homepage_bp
from routes.login import login_bp

app = Flask(__name__)
app.secret_key = "secret_key"

# REGISTRAR BLUEPRINTS
app.register_blueprint(homepage_bp)
app.register_blueprint(login_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)