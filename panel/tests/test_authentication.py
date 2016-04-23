from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


class AuthTestCase(TestCase):
  fixtures = ['test_data']

  def setUp(self):
    self.client = Client()

  def test_cannot_get_employees_if_not_authenticated(self):
    response = self.client.get(reverse('employees'))
    self.assertEqual(403, response.status_code)

  def test_cannot_get_allocations_if_not_authenticated(self):
    response = self.client.get(reverse('allocations'))
    self.assertEqual(403, response.status_code)

  def test_can_authenticate_with_fixture_data_and_use_api(self):
    self.client.login(username='test', password='testpassword')

    employees_response = self.client.get(reverse('employees'))
    self.assertEqual(200, employees_response.status_code)

    allocations_response = self.client.get(reverse('employees'))
    self.assertEqual(200, allocations_response.status_code)
