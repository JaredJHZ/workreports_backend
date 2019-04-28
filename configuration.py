import os
def get_key():
    key = "key123"
    if 'key' in os.environ:
        key = os.environ['key']
    return key