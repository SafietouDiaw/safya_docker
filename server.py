import os
import connexion
from models import db, ma

basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__, specification_dir=basedir)
app = connex_app.app

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'inventory.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
ma.init_app(app)

connex_app.add_api("swagger.yml", base_path="/api")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    connex_app.run(host="0.0.0.0", port=5000)
