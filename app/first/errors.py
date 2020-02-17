from flask import render_template
from . import main

# Error handler decorator
@main.app_errorhandler(404)
def four_ow_four(error):
    '''
    Function to render the 404 error page
    '''
    title = '404 page'
    return render_template('fourowfour', title=title),404