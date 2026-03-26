CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    book_type TEXT,
    book_name TEXT,
    writer TEXT,
    review TEXT,
    grade INTEGER,
    user_id INTEGER REFERENCES users
);