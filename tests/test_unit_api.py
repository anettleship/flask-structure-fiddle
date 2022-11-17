from app.models import User
from api.api import get_next_id, add_user, read_table_full, write_table


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


def test_get_next_id_empty(add_db_empty):

    app, db = add_db_empty
    next_id = get_next_id(db, User)
    assert next_id == 0


def test_get_next_id_single(add_db_user):

    app, db = add_db_user
    next_id = get_next_id(db, User)
    assert next_id == 1


def test_get_next_id_multiple(add_db_users):

    app, db = add_db_users
    next_id = get_next_id(db, User)
    assert next_id == 3


def test_add_user_empty():

    assert True == True


# Todo build out above test and test other functions in api
# Next module, write tests first, write code later


def test_read_table_full_empty(add_db_empty):

    app, db = add_db_empty
    user_data = read_table_full(db, User, User.id)

    assert len(user_data) == 0


def test_read_table_full_single(add_db_user):

    app, db = add_db_user
    user_data = read_table_full(db, User, User.id)

    assert len(user_data) == 1


def test_read_table_full_multiple(add_db_users):

    app, db = add_db_users
    user_data = read_table_full(db, User, User.id)

    assert len(user_data) == 3


