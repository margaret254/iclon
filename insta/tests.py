from django.test import TestCase

# Create your tests here.

class PostTestClass(TestCase):
    def setUp(self):
        self.maggie=Profile(title='maggie',Bio='testing')
        self.maggie.save_editor()

        self.new_post=Post(title='serah',post='testing',profile = self.maggie)
        self.new_post.save()

    def tearDown(self):
        Profile.objects.all().delete()
        Post.objects.all().delete()

    def test_get_new_posts(self):
        new_posts = Post.new_posts()
        self.assertTrue(len(new_posts)>0)