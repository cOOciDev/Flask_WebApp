
from flask import Blueprint, render_template, request

bp = Blueprint('contactUs', __name__)

@bp.route('/contactUs', methods=['GET', 'POST'])
def contactUs():
    if request.method == 'POST':
        # Handle POST request (if needed)
        pass    
    return render_template('contactUs.html')


