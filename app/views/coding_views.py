from flask import Blueprint, render_template, request

bp = Blueprint('coding', __name__)

@bp.route('/coding', methods=['GET', 'POST'])
def coding():
    if request.method == 'POST':
        # Handle POST request (if needed)
        pass    
    return render_template('coding.html')