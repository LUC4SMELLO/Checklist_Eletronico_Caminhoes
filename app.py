from flask import Flask

from routes.homepage import homepage_bp
from routes.checklist_html import checklist_bp
from routes.checklist_post import checklist_post_bp
from routes.login import login_bp
from routes.cadastro import cadastro_bp

app = Flask(__name__)
app.register_blueprint(homepage_bp)
app.register_blueprint(checklist_bp)
app.register_blueprint(checklist_post_bp)
app.register_blueprint(login_bp)
app.register_blueprint(cadastro_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
