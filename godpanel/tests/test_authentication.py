from django.core.urlresolvers import reverse
from django.test import Client

from godpanel.tests.constants import *
from godpanel.tests.godpanel_test_case import GodpanelTestCase


class AuthTestCase(GodpanelTestCase):
    def setUp(self):
        self.client = Client()

    def test_cannot_get_employees_if_not_authenticated(self):
        response = self.client.get(reverse('godpanel.employees'))
        self.assertEqual(HTTP_FORBIDEN, response.status_code)

    def test_cannot_get_allocations_if_not_authenticated(self):
        response = self.client.get(reverse('godpanel.allocations'), {
            'start': '2016-04-20',
            'end': '2016-04-23'
        })
        self.assertEqual(HTTP_FORBIDEN, response.status_code)

    def test_can_authenticate_with_fixture_data_and_use_api(self):
        self.client.login(username=TEST_USERNAME, password=TEST_PASSWORD)

        employees_response = self.client.get(reverse('godpanel.employees'))
        self.assertEqual(HTTP_OK, employees_response.status_code)

        allocations_response = self.client.get(reverse('godpanel.employees'))
        self.assertEqual(HTTP_OK, allocations_response.status_code)
