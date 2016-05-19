import json

from django.core.urlresolvers import reverse
from django.test import Client

from godpanel.tests.constants import *
from godpanel.tests.godpanel_test_case import GodpanelTestCase
from godpanel.models import Allocation


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
            'start': '2016-05-02',
            'end': '2016-06-01'
        })
        json_response = json.loads(allocations.content.decode())

        self.assertEqual(2, len(json_response))

        allocation = json_response.pop()

        # assert all the json keys in the response
        self.assertTrue(ALLOCATIONS_RESPONSE_FIELDS == set(allocation.keys()))

    def test_it_can_update_allocations(self):
        # data for api test request
        id = 1
        start = '2016-01-01'
        end = '2016-01-10'

        request_data = {
            'id': id,
            'start': start,
            'end': end
        }
        content_type = 'application/json'

        # verify response from api
        response = self.client.put(reverse('godpanel.allocations'), data=json.dumps(request_data), content_type=content_type)
        response_object = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response_object['message'], 'resource %d updated' % (id))

        # fetch object from db and verify it's been updated
        allocation = Allocation.objects.get(pk=id)

        self.assertEqual(allocation.start.isoformat(), start)
        self.assertEqual(allocation.end.isoformat(), end)

    def test_it_fetches_empty_allocations_if_dates_out_of_range(self):
        allocations = self.client.get(reverse('godpanel.allocations'), {
            'start': '2015-05-20',
            'end': '2015-05-23'
        })
        json_response = json.loads(allocations.content.decode())

        self.assertEqual(0, len(json_response))

    def test_start_and_end_parameters_are_required(self):
        # note: no query string params in get request
        allocations = self.client.get(reverse('godpanel.allocations'))

        self.assertEqual(400, allocations.status_code)
