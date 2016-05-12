# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from ..models import File
from ..views import get_file


class ViewTestCase(TestCase):

	def setUp(self):
		self.no_file = File(slug='no_file')
		self.no_file.save()

		f = SimpleUploadedFile("test.txt", "file_content")
		self.with_file = File(slug='with_file', content=f)
		self.with_file.save()


	def test_no_file(self):
		# no file assosiated with instance
		self.assertRaises(ValueError, get_file, None, 'no_file')
		

	def test_with_file(self):
		# test getting not empty file
		response = get_file(None, 'with_file')
		content = "attachment; filename={} - {}".format(self.with_file.content, self.with_file.slug)

		self.assertEqual(response['Content-Disposition'], content)