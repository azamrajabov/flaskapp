from app.models.user import User
from app.models.post import Post
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
