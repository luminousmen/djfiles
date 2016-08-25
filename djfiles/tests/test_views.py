# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from ..models import File
from ..views import get_file


class ViewTestCase(TestCase):

	def setUp(self):
		self.no_file = File(slug='no_file')
		self.no_file.save()

		self.f = open("test.txt", 'wb')
		self.f.write(str("file_content").encode('utf-8'))
		self.f = open("test.txt", 'rb')

		f = SimpleUploadedFile("test.txt", self.f.read())
		self.with_file = File(slug='with_file', content=f)
		self.with_file.save()

	def test_no_file(self):
		# no file assosiated with instance
		self.assertRaises(ValueError, get_file, None, 'no_file')

	def tearDown(self):
		self.no_file.delete()
		self.with_file.delete()
