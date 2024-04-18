#!/usr/bin/env python3
""" Handles API authentication using sessions. """


from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth (Auth):
    """ Manages user authentication through sessions. """
    #user_id_by_session_id = {}
    pass
