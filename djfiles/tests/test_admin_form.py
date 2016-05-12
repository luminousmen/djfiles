# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from ..admin import FileAdmin, FileForm
from ..models import File


class ModelAdminTests(TestCase):


	def test_validate_empty_form(self):
		form = FileForm()
		
		self.assertFalse(form.is_valid())


	def test_validate_full_form(self):
		uploadedfile = SimpleUploadedFile("test.txt", "file_content")
		form = FileForm({'slug': 'test'}, {'content': uploadedfile})

		self.assertTrue(form.is_valid())


	def test_save_form(self):
		uploadedfile = SimpleUploadedFile("test.txt", "file_content")
		form = FileForm({'slug': 'test'}, {'content': uploadedfile})
		obj = form.save()
		
		self.assertEqual('text/plain', obj.mime_type)
		self.assertEqual(u'test', obj.slug)
		self.assertNotEqual(None, obj.content)