from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
# Create your views here.
from django.http import HttpResponse

from index.models import *
from collections import defaultdict
import urllib
from index.btparse import decode as btdecode
import traceback

def binify(data):
    return '%' + '%'.join((data[i:i+2] for i in range(0, len(data), 2)))


def get_stats(request):
    torrents = Torrent.objects.all().order_by("-date")
    d = defaultdict(list)
    for t in torrents:
        try: 
            d[t.trackers.first()].append(t.info_hash)
        except:
            traceback.print_exc()
    
    for key in d.keys():
        new_url = str(key).replace('announce','scrape') + '?info_hash='
        hashes = d[key]
        new_url += '&info_hash='.join(binify(i) for i in hashes)
        try:
            data = urllib.urlopen(new_url).read()
            formatted_data = btdecode(data)
            files = formatted_data['files']
            for f in files.keys():
                g = files[f]
                stat = TorrentStat(info_hash=''.join(r'{0:02x}'.format(ord(c)) for c in f), seeders=g['complete'], leechers=g['incomplete'], completed=g['downloaded'])
                stat.save()
        except:
            traceback.print_exc()
    return HttpResponse(status=200)

def main(request):
    torrents = Torrent.objects.all().order_by("-date")
    render_objs = []
    for t in torrents:
        d = {'name':t.name, 'size':t.size, 'date':t.date, 'seeders':0, 'leechers':0, 'completed':0}
        stats = TorrentStat.objects.filter(info_hash=t.info_hash).order_by('-query_date')
        if stats:
            stat = stats.first()
            d['seeders'] = stat.seeders
            d['leechers'] = stat.leechers
            d['completed'] = stat.completed
        render_objs.append(d)
    return render_to_response("index.jade", dict(torrents=render_objs))
