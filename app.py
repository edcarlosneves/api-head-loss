from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import User
from resources.head_loss import HeadLoss, GetHeadLoss

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False
# app.config['SECRET_KEY'] = 'super-secret'
app.secret_key = "perdacarga"
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(HeadLoss, "/headloss")
api.add_resource(User, "/user/<string:username>")
api.add_resource(GetHeadLoss, "/headloss/<int:analysis_id>")

if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(port=5123, debug=True)
