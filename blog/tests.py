from django.test import TestCase
from django.http import response
from django.contrib.auth.models import AnonymousUser, User
from django.utils import timezone

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

# Test for requesting the post edit page
    def test_post_edit_page_reachable(self):
        '''
        Make sure the post edit page is reachable
        '''
        create_post('Test title', 'Test text')
        response = self.client.get('/post/1/edit/')
        self.assertEqual(response.status_code, 200)

# Test for creating a new post

# Test for editing an existing post

# Test for deleting an existing post

# Test for creating a new comment

# Test for deleting an existing comment