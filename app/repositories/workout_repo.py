from app.db import get_db

class WorkoutRepository:
    def create_workout(self, user_id, date, notes):
        db = get_db()
        cursor = db.execute(
            "INSERT INTO workout (user_id, date, notes) VALUES (?, ?, ?)",
            (user_id, date, notes)
        )
        db.commit()
        return cursor.lastrowid # Restituisce l'ID del workout creato

    def get_all_by_user(self, user_id):
        # Query complessa: Unisce workout e calcola il volume totale (reps * weight)
        # Livello Pro: GROUP BY e SUM
        sql = """
        SELECT w.id, w.date, w.notes, 
               COALESCE(SUM(ws.reps * ws.weight), 0) as total_volume
        FROM workout w
        LEFT JOIN workout_set ws ON w.id = ws.workout_id
        WHERE w.user_id = ?
        GROUP BY w.id
        ORDER BY w.date DESC
        """
        db = get_db()
        return db.execute(sql, (user_id,)).fetchall()

    def get_workout_details(self, workout_id, user_id):
        db = get_db()
        # Verifica che il workout appartenga all'utente
        workout = db.execute(
            "SELECT * FROM workout WHERE id = ? AND user_id = ?", 
            (workout_id, user_id)
        ).fetchone()
        
        if not workout:
            return None, []

        # Recupera i set collegati
        sets = db.execute("""
            SELECT ws.*, e.name as exercise_name, e.muscle_group
            FROM workout_set ws
            JOIN exercise e ON ws.exercise_id = e.id
            WHERE ws.workout_id = ?
        """, (workout_id,)).fetchall()
        
        return workout, sets

    def add_set(self, workout_id, exercise_id, reps, weight):
        db = get_db()
        db.execute(
            "INSERT INTO workout_set (workout_id, exercise_id, reps, weight) VALUES (?, ?, ?, ?)",
            (workout_id, exercise_id, reps, weight)
        )
        db.commit()

    def get_exercises(self):
        db = get_db()
        return db.execute("SELECT * FROM exercise").fetchall()