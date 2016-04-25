from panel.tests.godpanel_test_case import GodpanelTestCase
from django.test import Client
from django.core.urlresolvers import reverse
from panel.tests.constants import *


class AuthTestCase(GodpanelTestCase):
    def setUp(self):
        self.client = Client()

    def test_is_redirected_to_homepage_if_not_authenticated(self):
        frontpage = self.client.get(reverse('frontpage'))
        self.assertEqual(HTTP_REDIRECT, frontpage.status_code)

    def test_can_see_homepage_if_authenticated(self):
        self.client.login(username=TEST_USERNAME, password=TEST_PASSWORD)
        frontpage = self.client.get(reverse('frontpage'))
        self.assertEqual(HTTP_OK, frontpage.status_code)