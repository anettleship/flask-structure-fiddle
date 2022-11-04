# flask-structure-fiddle

How to launch:

SECRET_KEY must be set as an environment variable before launch.

    set SECRET_KEY=keepmysecretkeysecretplease


A proof of concept Flask app to play with Flask features such as Blueprints and Database models and revise Flask application layout following an externally prescribed structure.

I started off working from this article and adopted the structure proposed here:
https://realpython.com/flask-blueprint/

I then added tests following the structure proposed here:
https://testdriven.io/blog/flask-pytest/

I followed this article to guide how to implement my config as a class in config.py, and to guide how to implement an application factory pattern for testing:
https://towardsdatascience.com/how-to-set-up-a-production-grade-flask-application-using-application-factory-pattern-and-celery-90281349fb7a



Project File Structure:

api
    blueprint for apis for programmatic access live here
generic
    blueprint for generic application functions for testing live here, if this were a real app, there would be more of these for different application functions, e.g. auth, search UI, sign up
static
    static files live here
tests
    test_functional_* files containing functional tests for individual routes implemented using pytest live here
    test_unit_* files containing unit tests for individual functions live here  
app.py
    calls application launch and registers blueprints, imported from supporting files
app
    app_factory.py
        contains application factory functions that are called by tests and app.py to instantiate flask applications
    config.py
        contains classes for different configuration options to allow for production launch and testing instances
    models.py
        contains schemas for database


Structure of a single blueprint: (following https://realpython.com/flask-blueprint/)

blueprint_name
    - static
        staticfile.js
    - templates
        - blueprint_name
            templatefile.html
    __init__.py
    blueprint_name.py
