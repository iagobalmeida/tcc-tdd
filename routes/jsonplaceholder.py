from fastapi import APIRouter, Header, Body
from connectors import jsonplaceholder

router = APIRouter()

@router.post('/authenticate')
def post_user_authenticate(user_email:str=Body(None), user_password:str=Body(None)):
    return jsonplaceholder.post_user_authenticate(user_email, user_password) 


@router.get('/users/{user_id}')
def get_user_data(user_id, token:str=Header(None)):
    return jsonplaceholder.get_user_data(token, user_id) 


@router.get('/users/{user_id}/posts')
def get_user_posts(user_id, token:str=Header(None)):
    return jsonplaceholder.get_user_posts(token, user_id)


@router.get('/users/public/{user_email}')
def public_get_user_data(user_email:str):
    return jsonplaceholder.public_get_user_data(user_email)


@router.get('/posts')
def public_get_posts():
    return jsonplaceholder.public_get_posts()


@router.get('/posts/{post_id}/comments')
def get_post_comments(post_id: int, token:str=Header(None)):
    return jsonplaceholder.get_post_comments(token, post_id)




