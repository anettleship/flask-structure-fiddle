import ast
import app.config as config
from app.app_factory import db
from app.app_factory import create_app
from tests.conftest import test_user, test_user1, test_user2


def test_users_single(test_user):
    """
    GIVEN a Flask application configured for testing and a blank database
    WHEN we add a single user to the database
    THEN check that user is the only item returned by the /users route in the api module
    """

    app = create_app(config.testing())
     
    with app.app_context():
        db.session.add(test_user)
        db.session.commit()

        # Create a test client using the Flask application configured for testing
        with app.test_client() as test_client:
            response = test_client.get("/users")
            assert response.status_code == 200
            assert ast.literal_eval(response.text)[0] == 'FlaskIsAwesome'
            assert len(ast.literal_eval(response.text)) == 1




def test_users_multiple(test_user, test_user1, test_user2):
    """
    GIVEN a Flask application configured for testing and a blank database
    WHEN we add a single user to the database
    THEN check that user is the only item returned by the /users route in the api module
    """

    app = create_app(config.testing())

    with app.app_context():
        db.session.add(test_user)
        db.session.add(test_user1)
        db.session.add(test_user2)
        db.session.commit()

        # Create a test client using the Flask application configured for testing
        with app.test_client() as test_client:
            response = test_client.get("/users")
            assert response.status_code == 200
            assert ast.literal_eval(response.text)[0] == 'FlaskIsAwesome'
            assert ast.literal_eval(response.text)[1] == 'FlaskIsAwesome1'
            assert ast.literal_eval(response.text)[2] == 'FlaskIsAwesome2'
            assert len(ast.literal_eval(response.text)) == 3



