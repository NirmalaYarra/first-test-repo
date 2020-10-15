from user import User

def authenticate(username,password):
    username = User.find_user_by_name(username,None)
    if user and safe_str_cmp(user.password,password):
        return user
def identity(payload):
    user_id = userid_mapping.get(payload)
    return User.find_user_by_id( user_id,None)