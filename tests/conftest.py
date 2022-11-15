# Shared fixtures live here
import pytest
# we must import app_factory before importing our models, so the db object on which models relies is instantiated.
from app.app_factory import db
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

