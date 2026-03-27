import db

def add_item(book_type, book_name, writer, review, grade, user_id):
    sql = """INSERT INTO items (book_type, book_name, writer, review, grade, user_id)
             VALUES (?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [book_type, book_name, writer, review, grade, user_id])

def get_items():
    sql = "SELECT id, book_name, writer FROM items ORDER BY id DESC"

    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.book_type,
                    items.book_name,
                    items.writer,
                    items.review,
                    items.grade,
                    users.username
             FROM items, users
             WHERE items.user_id = users.id AND
                   items.id = ?"""
    return db.query(sql, [item_id])[0]