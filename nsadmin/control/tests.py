from django.core.urlresolvers import reverse
from django.test import TestCase


class PlaylistMethodTests(TestCase):
	def test_example(self):
		self.assertEqual(True, True)


class PlaylistViewTests(TestCase):
	def test_view_example(self):
		response = self.client.get(reverse('control:index'))
		self.assertEqual(response.status_code, 200)