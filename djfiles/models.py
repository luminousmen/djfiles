# -*- coding: utf-8 -*-

import os

from slugify import slugify

from django.db import models
from django.db.models.signals import pre_delete, pre_save


def on_delete(sender, instance, **kwargs):
    for field in instance._meta.get_fields():
        if field and isinstance(field, models.FileField):
            fieldfield = getattr(instance, field.name)
            fieldfield.delete(False)


def on_save(sender, instance, **kwargs):
    if not instance.id:
        return

    if getattr(instance, '_pre_save_called_times', False):
        initial = sender.objects.get(pk=instance.id)

        for field in instance._meta.get_fields():
            if field and isinstance(field, models.FileField):
                new_value = getattr(instance, field.name)
                old_value = getattr(initial, field.name)
                if old_value and old_value != new_value:
                    old_value.delete(False)

    instance._pre_save_called_times = True


def cleanup(cls):
    uid = cls.__name__
    pre_delete.connect(receiver=on_delete, sender=cls, dispatch_uid=uid)
    pre_save.connect(receiver=on_save, sender=cls, dispatch_uid=uid)
    return cls


def file_upload_to(instance, filename):
    name, ext = os.path.splitext(filename)
    filename = '{}{}'.format(slugify(name, only_ascii=True), ext)
    return os.path.join('files', filename)


@cleanup
class File(models.Model):

    slug = models.SlugField(unique=True)
    mime_type = models.CharField(
        max_length=128, null=True, blank=True)
    content = models.FileField(upload_to=file_upload_to)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.slug

    def preview(self):

        if self.mime_type:
            if self.mime_type.startswith('image/'):
                preview = u'<img src="{0}" style="max-width: 50%">'
                return preview.format(self.content.url)
            return self.mime_type
        return '-'

    preview.allow_tags = True

    def url(self):
        return u'<a href="{0}">{0}</a>'.format(self.content.url)
    url.allow_tags = True

    class Meta:
        db_table = 'files'
        verbose_name = 'file'
        verbose_name_plural = 'files'
