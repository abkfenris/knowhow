"""
Main public blueprint for knowhow
"""

from flask import Blueprint

main = Blueprint('main', __name__)

# importing views for blueprint
from . import views  # noqa
