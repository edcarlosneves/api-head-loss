import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
from libs.strings import gettext
from schemas.user import UserSchema

user_schema = UserSchema()


class User(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        "password", type=str, required=True, help="password is required."
    )

    def post(self, username):
        data = User.parser.parse_args()

        if UserModel.search_username(username):
            return {"message": gettext("user_username_exists")}, 400

        user = UserModel(username, data["password"])
        user.save_to_db()

        return {"message": gettext("user_created")}, 201

    def delete(self, username):
        user = UserModel.search_username(username)
        if user:
            user.delete_from_db()
            return {"message": gettext("user_deleted")}

        return {"message": gettext("user_not_found")}

    def get(self, username):
        user = UserModel.search_username(username)
        if user:
            return user_schema.dump(user)
        return {"message": gettext("user_not_found")}
