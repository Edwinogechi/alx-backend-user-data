#!/usr/bin/env python3
"""manage the API authentication"""

from flask import request
from typing import List, TypeVar
from auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth Class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """returns the Base64 part of the Authorization header"""
        if authorization_header is None or\
           type(authorization_header) is not str:
            return None
        hd = authorization_header.split(' ')

        return hd[1] if hd[0] == 'Basic' else None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """returns the decoded value of a Base64 string"""
        if base64_authorization_header is None or\
           type(base64_authorization_header) is not str:
            return None
        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('utf-8')
            return message
        except Exception:
            return None

if __name__ == '__main__':

    a = BasicAuth()

    #print(a.extract_base64_authorization_header(None))
    #print(a.extract_base64_authorization_header(89))
    #print(a.extract_base64_authorization_header("Holberton School"))
    #print(a.extract_base64_authorization_header("Basic Holberton"))
    #print(a.extract_base64_authorization_header("Basic SG9sYmVydG9u"))
    #print(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA=="))
    #print(a.extract_base64_authorization_header("Basic1234"))
    print(a.decode_base64_authorization_header(None))
    print(a.decode_base64_authorization_header(89))
    print(a.decode_base64_authorization_header("Holberton School"))
    print(a.decode_base64_authorization_header("SG9sYmVydG9u"))
    print(a.decode_base64_authorization_header("SG9sYmVydG9uIFNjaG9vbA=="))
    print(a.decode_base64_authorization_header(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA==")))

