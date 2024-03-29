from flask import Blueprint, render_template, request

bp = Blueprint('havesomefun', __name__)

@bp.route('/havesomefun', methods=['GET', 'POST'])
def havesomefun():
    if request.method == 'POST':
        # Handle POST request (if needed)
        pass    
    return render_template('havesomefun.html')