from flask import Blueprint, render_template, request

bp = Blueprint('cOOciAcademy', __name__)

@bp.route('/cOOciAcademy', methods=['GET', 'POST'])
def cOOciAcademy():
    if request.method == 'POST':
        # Handle POST request (if needed)
        pass    
    return render_template('cOOciAcademy.html')