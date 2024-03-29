from flask import Blueprint, render_template, request

bp = Blueprint('owner', __name__)

@bp.route('/owner', methods=['GET', 'POST'])
def owner():
    if request.method == 'POST':
        # Handle POST request (if needed)
        pass    
    return render_template('owner.html')