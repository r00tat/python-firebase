# -*- coding: utf-8 -*-
""" firebase client library """

MAJOR_VERSION = 0
MINOR_VERSION = 1
PATCH_LEVEL = 1

__version__ = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, PATCH_LEVEL)

from .client import Firebase
