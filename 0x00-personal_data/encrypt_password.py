#!/usr/bin/env python3
"""
    Secure Password Encryption
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Takes a password string and returns a salted, hashed password as a byte string.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password.
    """
    if password:
        return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if a password matches its hashed version.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The password to check.

    Returns:
        bool: True if the password matches its hash, False otherwise.
    """
    if hashed_password and password:
        return bcrypt.checkpw(str.encode(password), hashed_password)
