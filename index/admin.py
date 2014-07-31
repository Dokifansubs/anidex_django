from django.contrib import admin

# Register your models here.
from index.models import *

admin.site.register(Torrent)
admin.site.register(User)
admin.site.register(Group)
