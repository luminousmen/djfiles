# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os

from django.test import TestCase
from django.db.models import signals
from django.core.files.uploadedfile import SimpleUploadedFile

from ..admin import FileAdmin, FileForm
from ..models import File, on_save, on_delete


class ModelAdminTests(TestCase):

    def setUp(self):
        # creating empty file
        self.f = open("test.txt", 'wb')
        self.f.write(str("file_content").encode('utf-8'))
        self.f = open("test.txt", 'rb')

    def test_validate_empty_form(self):
        form = FileForm()

        self.assertFalse(form.is_valid())

    def test_validate_full_form(self):
        uploadedfile = SimpleUploadedFile("test.txt", self.f.read())
        form = FileForm({'slug': 'test'}, {'content': uploadedfile})

        self.assertTrue(form.is_valid())

    def test_save_form(self):
        # save valid admin form
        uploadedfile = SimpleUploadedFile("test.txt", self.f.read())
        form = FileForm({'slug': 'test'}, {'content': uploadedfile})
        self.obj = form.save()

        self.assertEqual('text/plain', self.obj.mime_type)
        self.assertEqual(u'test', self.obj.slug)
        self.assertNotEqual(None, self.obj.content)

        self.obj.delete()

    def test_save_signal(self):
        signals.pre_save.connect(on_save, weak=False)

        try:
            uploadedfile = SimpleUploadedFile("test.txt", self.f.read())
            f1 = File.objects.create(slug="test", content=uploadedfile)

            with self.assertRaises(AttributeError):
                # if instance wasn't saved then there is no attribute '_pre_save_called_times'
                f1._pre_save_called_times

            # save path to delete file after test
            path = f1.content.path

            f1.save()
            self.assertEqual(True, os.path.isfile(path))
            self.assertEqual(True, f1._pre_save_called_times)

        finally:
            f1.delete()
            signals.pre_save.disconnect(on_save)

    def test_delete_signal(self):
        signals.pre_delete.connect(on_delete, weak=False)

        try:
            uploadedfile = SimpleUploadedFile("test.txt", self.f.read())
            f1 = File.objects.create(slug="test", content=uploadedfile)
            path = f1.content.path
            f1.delete()

            # file not exist after delete
            self.assertEqual(False, os.path.isfile(path))

        finally:
            signals.pre_delete.disconnect(on_delete)

    def tearDown(self):
        import os
        os.remove("test.txt")
