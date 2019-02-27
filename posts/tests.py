from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse
from .models import Post
# Create your tests here.


class IndexPageTests(SimpleTestCase):

    def test_index_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


    def test_index_url_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_status_code(self):
        response = self.client.get('/about')
        self.assertEquals(response.status_code, 200)

    def test_about_url_name(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

class PostTests(TestCase):

    @classmethod
    def setUp(cls):
        Post.objects.create(title='We are learning laravel')


    def test_text(self):
        post = Post.objects.get(id=1)
        expected_post_title = post.title
        self.assertEquals(expected_post_title, 'We are learning laravel')


    def test_post_list_view(self):
        response = self.client.get(reverse('posts'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'We are learning laravel')
        self.assertTemplateUsed(response, 'posts.html')