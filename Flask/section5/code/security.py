from werkzeug.security import safe_str_cmp
from user import User

# when the user authenticates i.e sends in the auth endpoint with a username and password


def authenticate(username, password):
    # retrieve the user object using mapping and then compare the user's passowrd to the mapping password
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

# whenever they request an endpoint that needs to be authenticated, we use the identity
# method, so we get a pay load coming from the request and in that payload we get the identity
# which is the user id and there we retrieve the user object using the id mapping and if that
# doesn't match then we assume that the jwt token was correct, and the user therefore knows that he is
# logged in


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
