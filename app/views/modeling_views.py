
from flask import Blueprint, render_template, request

bp = Blueprint('modeling', __name__)

@bp.route('/modeling', methods=['GET', 'POST'])
def modeling():
    if request.method == 'POST':
        # Handle POST request (if needed)
        pass    
    return render_template('modeling.html')