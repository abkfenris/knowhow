"""
Main public routes for knowhow
"""

from . import main


@main.route('/')
def index():
    """
    Index page
    """
    return 'Hello World!'
