import os
from flask import Flask



class config:

    """
    Primary class that implements default values common to all configurations, may be overwritten by children.
    """

    def __init__(self):
        self.exists = True

        # Default settings
        self.FLASK_ENV = 'development'
        self.DEBUG = False
        self.TESTING = False

        # Do not set a default secret key, we want application launch to fail by default if none set as part of application health checks
        self.SECRET_KEY = os.getenv('SECRET_KEY') 

class testing(config):
    """
    Config for instantiating an app within software tests.
    """
    
    def __init__(self):
        # initialise base class to inherit properties
        super().__init__()
        self.FLASK_ENV = 'testing'
        self.TESTING = True 


class development(config):
    """
    Config for development
    """

    def __init__(self):
        # initialise base class to inherit properties
        super().__init__()
        self.DEBUG = True

class production(config):
    """
    Config for production 
    """

    def __init__(self):
        # initialise base class to inherit properties
        super().__init__()
        self.FLASK_ENV = 'production'




