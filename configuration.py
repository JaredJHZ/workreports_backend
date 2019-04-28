import os
def get_key():
    key = "key123"
    if os.environ['key']:
        key = os.environ['key']
    return key