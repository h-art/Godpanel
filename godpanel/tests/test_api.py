import json

from django.core.urlresolvers import reverse
from django.test import Client

from godpanel.tests.constants import *
from godpanel.tests.godpanel_test_case import GodpanelTestCase


class ApiTestCase(GodpanelTestCase):
    def setUp(self):
        self.client = Client()
        self.client.login(username=TEST_USERNAME, password=TEST_PASSWORD)

    def test_it_fetches_employees(self):
        employees = self.client.get(reverse('godpanel.employees'))
        json_response = json.loads(employees.content.decode())

        self.assertEqual(1, len(json_response))

        employee = json_response.pop()

        self.assertTrue(EMPLOYEES_RESPONSE_FIELDS == set(employee.keys()))

    def test_it_fetches_allocations(self):
        allocations = self.client.get(reverse('godpanel.allocations'), {
            'start': '2016-04-20',
            'end': '2016-04-23'
        })
        json_response = json.loads(allocations.content.decode())

        self.assertEqual(1, len(json_response))

        allocation = json_response.pop()

        self.assertTrue(ALLOCATIONS_RESPONSE_FIELDS == set(allocation.keys()))

    def test_it_fetches_empty_allocations_if_dates_out_of_range(self):
        allocations = self.client.get(reverse('godpanel.allocations'), {
            'start': '2015-04-20',
            'end': '2015-04-23'
        })
        json_response = json.loads(allocations.content.decode())

        self.assertEqual(0, len(json_response))

    def test_start_and_end_parameters_are_required(self):
        allocations = self.client.get(reverse('godpanel.allocations'))
        json_response = json.loads(allocations.content.decode())

        self.assertEqual(400, allocations.status_code)
