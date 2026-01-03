import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from app.repositories.user_repo import UserRepository

bp = Blueprint('auth', __name__, url_prefix='/auth')
user_repo = UserRepository()

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username or not password:
            error = 'Username e password richiesti.'
        elif not user_repo.create(username, generate_password_hash(password)):
            error = f"L'utente {username} è già registrato."

        if error is None:
            return redirect(url_for('auth.login'))
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = user_repo.get_by_username(username)
        error = None

        if user is None or not check_password_hash(user['password'], password):
            error = 'Credenziali non valide.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('main.dashboard'))
        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = user_repo.get_by_id(user_id)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view