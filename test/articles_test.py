import  unittest
from app.models import Articles
class ArticlesTest(unittest.TestCase):
    """
    Test class to test the behaviour of the articles class.
    """
    def setUp(self):
        """
        Set up method that is run everytime before every test.
        """
        self.new_article = Articles('Flix', 'Kurgatfelo', 'www.kurgatfelo.com', 'www.kurgatiimage.com','14/3/1995')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))