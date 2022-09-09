import json
from django.test import TestCase


class BlogViewsTest(TestCase):
    def test_blog_url_exists_at_desired_location(self):
        response = self.client.get('/blogs/list/')
        self.assertEqual(response.status_code, 200)

    def test_create_blog_negative(self):
        data = json.dumps({
            'name': 'test_name',
            'description': 'test_description',
            'file_field': None
        })
        response = self.client.post('/blogs/new/', data, content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 302)
