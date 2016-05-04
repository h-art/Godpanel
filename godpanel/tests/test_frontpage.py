from urllib.parse import urlparse

from django.core.urlresolvers import reverse
from django.test import Client

from godpanel.tests.constants import *
from godpanel.tests.godpanel_test_case import GodpanelTestCase


class FrontpageTestCase(GodpanelTestCase):
    def setUp(self):
        self.client = Client()

    def test_is_redirected_to_godpanel_if_get_root_path(self):
        root = self.client.get(reverse('root'))
        self.assertEqual(HTTP_REDIRECT, root.status_code)
        self.assertEqual(root.url, reverse('godpanel.frontpage'))

    def test_is_redirected_to_homepage_if_not_authenticated(self):
        frontpage = self.client.get(reverse('godpanel.frontpage'))
        self.assertEqual(HTTP_REDIRECT, frontpage.status_code)
        parsed_url = urlparse(frontpage.url)
        self.assertEqual(parsed_url.query, 'next=%s' % (reverse('godpanel.frontpage')))

    def test_can_see_homepage_if_authenticated(self):
        self.client.login(username=TEST_USERNAME, password=TEST_PASSWORD)
        frontpage = self.client.get(reverse('godpanel.frontpage'))
        self.assertEqual(HTTP_OK, frontpage.status_code)
