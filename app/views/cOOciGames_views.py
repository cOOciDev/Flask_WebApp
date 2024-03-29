from flask import Blueprint, render_template, request

bp = Blueprint('cOOciGames', __name__)

@bp.route('/cOOciGames', methods=['GET', 'POST'])
def cOOciGames():
    if request.method == 'POST':
        # Handle POST request (if needed)
        pass    
    return render_template('cOOciGames.html')