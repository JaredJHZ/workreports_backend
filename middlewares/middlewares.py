import jwt
from configuration import key
def authentication(token):
    try:
        info = jwt.decode(token,key)
        return info
    except:
        return False