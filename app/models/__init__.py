from app import login, db
from app.models.user import User
from app.models.post import Post


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
