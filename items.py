import db

def add_item(book_type, book_name, writer, review, grade, user_id):
    sql = """INSERT INTO items (book_type, book_name, writer, review, grade, user_id)
            VALUES (?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [book_type, book_name, writer, review, grade, user_id])