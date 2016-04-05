from django.test import TestCase

# Create your tests here.
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

class QuestionTests(APITestCase):
    def test_create_question(self):
        """
        Ensure we can create a new Question object.
        """

        data = {'question_text': 'DabApps'}
        response = self.client.post('http://localhost:8000/questions/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
