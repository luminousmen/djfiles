# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms

from .models import File


class FileForm(forms.ModelForm):

    def save(self, *a, **kw):
        kw.update({'commit': False})
        instance = super(FileForm, self).save(*a, **kw)

        # InMemoryUploadedFile at first save FileField otherwise
        data = self.cleaned_data['content']
        instance.mime_type = getattr(data, 'content_type',
            instance.mime_type)

        instance.save()
        return instance

    class Meta:
        model = File
        fields = '__all__'


@admin.register(File)
class FileAdmin(admin.ModelAdmin):

    list_display = ('slug', 'url', 'description')
    readonly_fields = ('url', 'preview', 'mime_type')
    search_fields = ('slug',)
    form = FileForm
