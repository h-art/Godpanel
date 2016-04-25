from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from panel.tests.constants import *


class AuthTestCase(TestCase):
    fixtures = TEST_FIXTURES

    def setUp(self):
        self.client = Client()

    def test_cannot_get_employees_if_not_authenticated(self):
        response = self.client.get(reverse('employees'))
        self.assertEqual(HTTP_FORBIDEN, response.status_code)

    def test_cannot_get_allocations_if_not_authenticated(self):
        response = self.client.get(reverse('allocations'))
        self.assertEqual(HTTP_FORBIDEN, response.status_code)

    def test_can_authenticate_with_fixture_data_and_use_api(self):
        self.client.login(username=TEST_USERNAME, password=TEST_PASSWORD)

        employees_response = self.client.get(reverse('employees'))
        self.assertEqual(HTTP_OK, employees_response.status_code)

        allocations_response = self.client.get(reverse('employees'))
        self.assertEqual(HTTP_OK, allocations_response.status_code)
