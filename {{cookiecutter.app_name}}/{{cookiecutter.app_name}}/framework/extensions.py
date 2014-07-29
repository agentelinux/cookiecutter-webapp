# -*- coding: utf-8 -*-                                                                                       
"""
    application.extensions
    ~~~~~~~~~~~~~~~~~~~~~~

    Each extension is initialized in the app factory.

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.migrate import Migrate
migrate = Migrate()

from flask.ext.jwt import JWT
jwt = JWT()

#from flask.ext.mail import Mail
#mail = Mail()

#from flask.ext.security import Security
#security = Security()
