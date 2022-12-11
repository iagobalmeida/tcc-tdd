import jwt
from routes.jsonplaceholder import post_user_authenticate, get_user_data, get_user_posts, get_post_comments, public_get_user_data, public_get_posts

JWT_SECRET = 'json_placeholder'
USER_EMAIL = 'Sincere@april.biz'
USER_PASSWORD = 'Bret'
TOKEN = ''
USER_ID = '1'
POST_ID = '1'

def user_authenticate():
    token = post_user_authenticate(USER_EMAIL, USER_PASSWORD)
    return token


def test_user_authenticate():
    token = user_authenticate()
    token_data = jwt.decode(token, JWT_SECRET, algorithms="HS256")
    assert token_data['email'] == USER_EMAIL


def test_user_data():
    token = user_authenticate()
    user_data = get_user_data(token, USER_ID)
    assert 'id' in user_data
    assert 'email' in user_data
    assert 'name' in user_data
    assert 'username' in user_data
    assert 'address' in user_data
    assert 'phone' in user_data
    assert 'website' in user_data
    assert 'company' in user_data
    assert user_data['email'] == USER_EMAIL


def test_user_posts():
    token = user_authenticate()
    user_posts = get_user_posts(token, USER_ID)
    post = user_posts[0]
    assert 'id' in post
    assert 'title' in post
    assert 'body' in post
    assert 'userId' in post
    assert int(post['userId']) == int(USER_ID)


def test_post_comments():
    token = user_authenticate()
    post_comments = get_post_comments(token, POST_ID)
    comment = post_comments[0]
    assert 'id' in comment
    assert 'name' in comment
    assert 'email' in comment
    assert 'body' in comment
    assert 'postId' in comment
    assert int(comment['postId']) == int(POST_ID)


def test_public_user():
    user_data = public_get_user_data(USER_EMAIL)
    assert 'email' in user_data
    assert 'name' in user_data
    assert not 'username' in user_data
    assert not 'address' in user_data
    assert not 'company' in user_data
    assert not 'phone' in user_data


def test_public_posts():
    posts_data = public_get_posts()
    post = posts_data[0]
    assert 'id' in post
    assert 'title' in post
    assert 'body' in post
    assert 'userId' in post
    assert 'comments' in post
    assert int(post['userId']) == int(USER_ID)