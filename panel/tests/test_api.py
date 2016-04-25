import json
from panel.tests.godpanel_test_case import GodpanelTestCase
from django.test import Client
from django.core.urlresolvers import reverse
from panel.tests.constants import *


class ApiTestCase(GodpanelTestCase):
    def setUp(self):
        self.client = Client()
        self.client.login(username=TEST_USERNAME, password=TEST_PASSWORD)

    def test_it_fetches_employees(self):
        employees = self.client.get(reverse('employees'))
        json_response = json.loads(employees.content.decode())

        self.assertEqual(1, len(json_response))

        employee = json_response.pop()

        self.assertTrue(EMPLOYEES_RESPONSE_FIELDS == set(employee.keys()))

    def test_it_fetches_allocations(self):
        allocations = self.client.get(reverse('allocations'))
        json_response = json.loads(allocations.content.decode())

        self.assertEqual(1, len(json_response))

        allocation = json_response.pop()

        self.assertTrue(ALLOCATIONS_RESPONSE_FIELDS == set(allocation.keys()))
