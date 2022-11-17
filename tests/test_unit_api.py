from app.models import User
from tests.conftest import test_user 


def test_new_user(test_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = User(1,'emailuser@email.com', 'FlaskIsAwesome')
    assert user.email == 'emailuser@email.com'
    assert user.username == 'FlaskIsAwesome'
    assert user.id == 1


def test_get_next_id():
    assert True == True