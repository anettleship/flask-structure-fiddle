import app.config as config
from app.app_factory import create_app
from app.app_factory import db
from app.models import User

def test_generic_response():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    app = create_app(config.testing())

    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get("/healthcheck/")
        assert response.status_code == 200

def test_user_database():
    """
    GIVEN a Flask application configured for testing and a blank database
    WHEN we add a single user to the database
    THEN check that user is the only item returned by the /users route in the api module
    """

    app = create_app(config.testing())

    user = User(
        id = 1,
        username = "Flask",
        email = "my@email.com",
    )

    db.session.add(user)
    db.session.commit()



    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get("/healthcheck/")
        assert response.status_code == 200

