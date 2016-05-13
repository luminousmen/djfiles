# -*- coding: utf-8 -*-

from django.test import TestCase

from ..models import File


class ModelTestCase(TestCase):

	def setUp(self):
		self.no_slug_file = File.objects.create(slug='test')


	def test_model_name(self):
		self.assertEqual(self.no_slug_file.__class__.__name__, 'File')


	def test_save_file(self):
		self.no_slug_file.save()
		f = File.objects.get(pk=1)
		self.assertEqual(f.slug, 'test')


	def tearDown(self):
		self.no_slug_file.delete()