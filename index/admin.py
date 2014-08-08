from django.contrib import admin

# Register your models here.
from index.models import *

admin.site.register(Torrent)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Tracker)
admin.site.register(TorrentStat)
admin.site.register(TorrentFile)
