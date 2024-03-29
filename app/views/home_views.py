
from flask import Blueprint, render_template, request

bp = Blueprint('home', __name__)

@bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle POST request (if needed)
        pass
    return render_template('home.html')