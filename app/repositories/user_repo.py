from app.db import get_db

class UserRepository:
    def create(self, username, password_hash):
        db = get_db()
        try:
            db.execute(
                "INSERT INTO user (username, password) VALUES (?, ?)",
                (username, password_hash),
            )
            db.commit()
            return True
        except db.IntegrityError:
            return False

    def get_by_username(self, username):
        db = get_db()
        return db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

    def get_by_id(self, user_id):
        db = get_db()
        return db.execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()