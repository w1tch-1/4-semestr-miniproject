from django.test import TestCase
from models import Post

class IndexTestCase(TestCase):
    def test_db(self):
        post = Post.objects.create(title='test post', content='test contesnt')
        self.assertEqual(post.title, 'test post')
