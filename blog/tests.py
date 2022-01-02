from django.test import TestCase, Client
from django.http import response
from django.contrib.auth.models import AnonymousUser, User
from django.utils import timezone
from django.apps import apps

from .models import Post

# shortcuts:

def create_post(title, text):
    return Post.objects.create(title=title, text=text, author=User.objects.create(username='testuser'), published_date=timezone.now())


# Tests start here: 

class IndexPageTests(TestCase):

    def test_request_index_page(self):
        '''
        Make sure the homepage is reachable
        '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_post_creation(self):
        '''
        Make sure the post creation is working
        '''
        create_post('Test title', 'Test text')
        self.assertTrue(Post.objects.filter(title='Test title').exists())

    def test_posts_are_visible(self):
        '''
        Make sure the posts are visible on the index page
        '''
        create_post('Test title', 'Test text')
        response = self.client.get('/')
        self.assertContains(response, 'Test title')


class PostDetailPageTests(TestCase):

    def test_individual_post_page(self):
        '''
        Make sure the individual post page is reachable
        '''
        create_post('Test title', 'Test text')
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)

    def test_post_edit_page_reachable(self):
        '''
        Make sure the post edit page is reachable
        '''
        create_post('Test title', 'Test text')
        response = self.client.get('/post/1/edit/')
        self.assertEqual(response.status_code, 200)

    def test_post_edit_page_contains_form(self):
        '''
        Make sure the post edit page contains the form
        '''
        create_post('Test title', 'Test text')
        response = self.client.get('/post/1/edit/')
        self.assertContains(response, '<form')

class PostEditPageTests(TestCase):
    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testeditor')[0])
    
    def test_post_edit_page_reachable(self):
        '''
        Make sure the post edit page is reachable
        '''
        create_post('Test title', 'Test text')
        response = self.client.get('/post/1/edit/')
        self.assertEqual(response.status_code, 200)

    def test_post_edit_page_contains_form(self):
        '''
        Make sure the post edit page contains the form
        '''
        create_post('Test title', 'Test text')
        response = self.client.get('/post/1/edit/')
        self.assertContains(response, '<form')

    def test_post_edit_page_contains_title(self):
        '''
        Make sure the post edit page contains the title
        '''
        create_post('Test title', 'Test text')
        response = self.client.get('/post/1/edit/')
        self.assertContains(response, 'Test title')

    def test_post_edit_page_contains_text(self):
        '''
        Make sure the post edit page contains the text
        '''
        create_post('Test title', 'Test text')
        response = self.client.get('/post/1/edit/')
        self.assertContains(response, 'Test text')


class BlogDataTestCase(TestCase):
    def setUp(self):

        # User
        self.user = User.objects.create_superuser(
            username='admin',
            email='admin@hellogithub.com',
            password='admin'
        )
        self.client.login(username='admin', password='admin')

        # publish test article
        self.post1 = Post.objects.create(
            author=self.user,
            title='Test title one',
            text='Test content one',
        )
        self.post1.publish()

    def test_editing_a_post_redirects_to_post_detail_page(self):
        '''
        Test that editing a post redirects to the post detail page
        '''
        response = self.client.post('/post/1/edit/', {'title': 'Edited title', 'text': 'Edited text', 'author': self.user})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/post/1/')

    def test_editing_a_post_changes_the_title(self):
        '''
        Test that editing a post changes the title
        '''
        self.client.post('/post/1/edit/', {'title': 'This title has changed', 'text': 'Edited text', 'author': self.user})
        self.assertEqual(Post.objects.get(pk=1).title, 'This title has changed')
# Test for deleting an existing post

# Test for creating a new comment

# Test for deleting an existing comment