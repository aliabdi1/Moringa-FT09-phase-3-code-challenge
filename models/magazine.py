from database.connection import get_db_connection

class Magazine:
    def __init__(self, id=None, name=None, category=None):
        if id:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
            record = cursor.fetchone()
            conn.close()
            if not record:
                raise ValueError(f"No magazine found with id={id}")
            self.id = record["id"]
            self.name = record["name"]
            self.category = record["category"]
        elif name and category:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
            conn.commit()
            self.id = cursor.lastrowid
            self.name = name
            self.category = category
            conn.close()
        else:
            raise ValueError("You must provide either an ID or all required fields (name, category).")

    def __repr__(self):
        return f"<Magazine {self.name}>"

    def get_articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def get_authors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT authors.id, authors.name
            FROM authors
            JOIN articles ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
        """, (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return authors
