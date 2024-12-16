from database.connection import get_db_connection

class Article:
    def __init__(self, id=None, title=None, content=None, author_id=None, magazine_id=None):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
        
        if id:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
            record = cursor.fetchone()
            conn.close()
            if not record:
                raise ValueError(f"No article found with id={id}")
            self.id = record["id"]
            self.title = record["title"]
            self.content = record["content"]
            self.author_id = record["author_id"]
            self.magazine_id = record["magazine_id"]
        elif title and content and author_id and magazine_id:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO articles (title, content, author_id, magazine_id)
                VALUES (?, ?, ?, ?)
            """, (title, content, author_id, magazine_id))
            conn.commit()
            self.id = cursor.lastrowid
            self.title = title
            self.content = content
            self.author_id = author_id
            self.magazine_id = magazine_id
            conn.close()
        else:
            raise ValueError("You must provide either an ID or all required fields (title, content, author_id, magazine_id).")

    def __repr__(self):
        return f"<Article {self.title}>"
