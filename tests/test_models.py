import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine
from database.setup import create_tables  # Import create_tables from setup

class TestModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create tables in the in-memory database for testing
        create_tables(testing=True)

    def test_author_creation(self):
        # Test creation of an author
        author = Author(name="John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        # Test creation of an article
        article = Article(title="Test Title", content="Test Content", author_id=1, magazine_id=1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        # Test creation of a magazine
        magazine = Magazine(name="Tech Weekly", category="Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

if __name__ == "__main__":
    unittest.main()
