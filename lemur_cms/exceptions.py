
"""
Exceptions raised by the LemurCMS code and the machinery for handling them.
"""

import logging
import os
import sys

import six
from django.core.exceptions import PermissionDenied
from django.core.management import color_style  # noqa
from django.utils import encoding
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages


class LemurCMSException(Exception):
    """Base exception class for distinguishing our own exception classes."""
    pass


class Http302(LemurCMSException):
    """Error class which can be raised from within a handler to cause an
    early bailout and redirect at the middleware level.
    """
    status_code = 302

    def __init__(self, location, message=None):
        self.location = location
        self.message = message


class NotAuthorized(LemurCMSException):
    """Raised whenever a user attempts to access a resource which they do not
    have permission-based access to (such as when failing the
    """
    status_code = 401


class NotAuthenticated(PermissionDenied, LemurCMSException):
    """Raised when a user is trying to make requests and they are not logged
    in.

    The included :class:`~horizon.middleware.HorizonMiddleware` catches
    ``NotAuthenticated`` and handles it gracefully by displaying an error
    message and redirecting the user to a login page.
    """
    status_code = 403


class NotFound(LemurCMSException):
    """Generic error to replace all "Not Found"-type API errors."""
    status_code = 404


class Conflict(LemurCMSException):
    """Generic error to replace all "Conflict"-type API errors."""
    status_code = 409


class RecoverableError(LemurCMSException):
    """Generic error to replace any "Recoverable"-type API errors."""
    status_code = 100  # HTTP status code "Continue"
