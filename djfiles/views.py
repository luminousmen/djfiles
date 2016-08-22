# -*- coding: utf-8 -*-

from django.shortcuts import redirect, get_object_or_404

from .models import File


def get_file(request, filename):

    f = get_object_or_404(File, slug=filename)
    return redirect(f.content.url)
