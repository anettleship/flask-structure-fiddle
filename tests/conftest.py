# Shared fixtures live here
import pytest
import app.config as config
# we must import app_factory before importing our models, so the db object on which models relies is instantiated.
from app.app_factory import db
from app.app_factory import create_app
from app.models import User


@pytest.fixture(scope='function')
def test_user():
    user = User(0,'emailuser@email.com', 'FlaskIsAwesome')
    return user


@pytest.fixture(scope='function')
def test_user1():
    user = User(1,'emailuser1@email.com', 'FlaskIsAwesome1')
    return user


@pytest.fixture(scope='function')
def test_user2():
    user = User(2,'emailuser2@email.com', 'FlaskIsAwesome2')
    return user


@pytest.fixture(scope='function')
def add_db_users(test_user, test_user1, test_user2):

    app = create_app(config.testing())

    with app.app_context():
        db.session.add(test_user)
        db.session.add(test_user1)
        db.session.add(test_user2)
        db.session.commit()

        yield app

