# -*- coding: utf-8 -*-

from django.http import HttpResponse

from .models import File


def get_file(request, filename):

    f = File.objects.get(slug=filename)
    fs = open(f.content.path, 'r')
    response = HttpResponse(fs)
    response['Content-Disposition'] = "attachment; filename={} - {}".format(f.content, f.slug)
    return response
