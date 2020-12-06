from werkzeug.security import check_password_hash
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.search_username(username)
    if user and check_password_hash(user.password, password):
        return user


def identity(payload):
    id_user = payload['identity']
    return UserModel.search_by_id(id_user)
