# Shared fixtures live here
import pytest
from app.models import User


@pytest.fixture(scope='module')
def new_user():
    user = User(1,'patkennedy79@gmail.com', 'FlaskIsAwesome')
    return user