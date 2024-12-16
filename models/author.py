from database.connection import get_db_connection

class Author:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
        if id:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
            record = cursor.fetchone()
            conn.close()
            if not record:
                raise ValueError(f"No author found with id={id}")
            self.id = record["id"]
            self.name = record["name"]
        elif name:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
            conn.commit()
            self.id = cursor.lastrowid
            self.name = name
            conn.close()
        else:
            raise ValueError("You must provide either an ID or a name.")

    def __repr__(self):
        return f"<Author {self.name}>"

    def get_articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def get_magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT magazines.id, magazines.name, magazines.category
            FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?
        """, (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines
