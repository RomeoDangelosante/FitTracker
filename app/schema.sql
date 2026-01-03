DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS workout;
DROP TABLE IF EXISTS exercise;
DROP TABLE IF EXISTS workout_set;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE exercise (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    muscle_group TEXT NOT NULL
);

CREATE TABLE workout (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE workout_set (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,
    reps INTEGER NOT NULL,
    weight REAL NOT NULL,
    FOREIGN KEY (workout_id) REFERENCES workout (id),
    FOREIGN KEY (exercise_id) REFERENCES exercise (id)
);

-- Dati iniziali (Seed)
INSERT INTO exercise (name, muscle_group) VALUES 
('Panca Piana', 'Petto'),
('Squat', 'Gambe'),
('Stacco da Terra', 'Schiena'),
('Curl Manubri', 'Bicipiti');