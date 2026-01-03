from flask import Blueprint, render_template, request, redirect, url_for, g, flash
from app.auth import login_required
from app.repositories.workout_repo import WorkoutRepository

# QUESTA è la riga che Python non trovava:
bp = Blueprint('main', __name__)

workout_repo = WorkoutRepository()

@bp.route('/')
@login_required
def dashboard():
    workouts = workout_repo.get_all_by_user(g.user['id'])
    return render_template('main/dashboard.html', workouts=workouts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        date = request.form['date']
        notes = request.form['notes']
        if not date:
            flash('La data è obbligatoria!')
        else:
            workout_id = workout_repo.create_workout(g.user['id'], date, notes)
            return redirect(url_for('main.details', id=workout_id))
    
    return render_template('main/create.html')

@bp.route('/workout/<int:id>', methods=('GET', 'POST'))
@login_required
def details(id):
    # Gestione aggiunta set (POST)
    if request.method == 'POST':
        exercise_id = request.form['exercise_id']
        reps = request.form['reps']
        weight = request.form['weight']
        workout_repo.add_set(id, exercise_id, reps, weight)
        flash('Serie aggiunta!')
        return redirect(url_for('main.details', id=id))

    # Visualizzazione (GET)
    workout, sets = workout_repo.get_workout_details(id, g.user['id'])
    exercises = workout_repo.get_exercises()
    
    if workout is None:
        return redirect(url_for('main.dashboard'))
        
    return render_template('main/details.html', workout=workout, sets=sets, exercises=exercises)