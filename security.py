from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload): #This function is unique to Flask-JWT, it takes in a payload which is contents of the JWT token sent to us
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)