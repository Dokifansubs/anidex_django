from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
# Create your views here.

from index.models import *

def main(request):
    torrents = Torrent.objects.all().order_by("-date")
    paginator = Paginator(torrents, 10)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("index.jade", dict(torrents=torrents))
