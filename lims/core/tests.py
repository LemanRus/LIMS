from django.test import TestCase


class WalkAroundCase(TestCase):
    def test_home_page_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_help_page_response(self):
        response = self.client.get('/help/')
        self.assertEqual(response.status_code, 200)
