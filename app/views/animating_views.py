
from flask import Blueprint, render_template, request

bp = Blueprint('animating', __name__)

@bp.route('/animating', methods=['GET', 'POST'])
def animating():
    if request.method == 'POST':
        # Handle POST request (if needed)
        pass    
    return render_template('animating.html')