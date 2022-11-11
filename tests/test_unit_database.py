from app.models import User
from tests.conftest import new_user


def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = User(1,'patkennedy79@gmail.com', 'FlaskIsAwesome')
    assert user.email == 'patkennedy79@gmail.com'
    assert user.username == 'FlaskIsAwesome'
    assert user.id == 1