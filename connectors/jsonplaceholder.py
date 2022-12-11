import jwt
import requests

JWT_SECRET = 'json_placeholder'
BASE_URL = 'https://jsonplaceholder.typicode.com'


def _get(route, params):
    req = requests.request('GET', f'{BASE_URL}/{route}', params=params)
    return req.json()


def _generate_token(user_data):
    return jwt.encode(user_data, JWT_SECRET, algorithm="HS256")


def _validate_token(token):
    try:
        data = jwt.decode(token, JWT_SECRET, algorithms='HS256')
        return data
    except:
        return None
    

def _publicize_user(user_data):
    del user_data['username']
    del user_data['address']
    del user_data['company']
    del user_data['phone']
    return user_data

    
def post_user_authenticate(user_email, user_password):
    user_by_email = _get('users', { 'email': user_email })[0]
    if not user_by_email: return None
    if user_by_email['username'] != user_password: return None
    token = _generate_token(user_by_email)
    return token


def get_user_data(user_id, token):
    token_data = _validate_token(token)
    if int(token_data['id']) != int(user_id): return None
    user_by_id = _get('users', { 'id': user_id })[0]
    return user_by_id


def get_user_posts(user_id, token):
    token_data = _validate_token(token)
    if int(token_data['id']) != int(user_id): return None
    posts_by_user_id = _get('posts', { 'userId': user_id })
    return posts_by_user_id


def get_post_comments(post_id, token):
    _validate_token(token)
    comments_by_post_id = _get('comments', { 'postId': post_id })
    return comments_by_post_id
        

def public_get_user_data(user_email):
    user_by_email = _get('users', {'email': user_email})[0]
    return _publicize_user(user_by_email)
