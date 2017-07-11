"""Application configuration goes here."""

import os.path as op

DEBUG = True

BASE_DIR = op.abspath(op.join(op.dirname(__file__), '..'))
STATIC_DIR = op.join(BASE_DIR, 'app', 'static')
