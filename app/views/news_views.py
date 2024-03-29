from flask import Blueprint, render_template, request

bp = Blueprint('news', __name__)

@bp.route('/news', methods=['GET', 'POST'])
def news():
    if request.method == 'POST':
        # Handle POST request (if needed)
        pass    
    return render_template('news.html')