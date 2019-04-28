import jwt
from configuration import get_key
def authentication(token):
    try:
        info = jwt.decode(token,get_key())
        return info
    except:
        return False