# Shared fixtures live here
import pytest
# we must import app_factory before importing our models, so the db object on which models relies is instantiated.
from app.app_factory import db
from app.models import User


@pytest.fixture(scope='module')
def test_user():
    user = User(1,'emailuser@email.com', 'FlaskIsAwesome')
    return user