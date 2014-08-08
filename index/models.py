from django.db import models
from datetime import datetime
# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)
    groups = models.ManyToManyField(Group)

    def __unicode__(self):
        return self.name

class Tracker(models.Model):
    url = models.CharField(max_length=200)

    def __unicode__(self):
        return self.url

class TorrentStat(models.Model):
    info_hash = models.CharField(max_length=40)
    query_date = models.DateTimeField(default=datetime.utcnow, blank=True)
    seeders = models.IntegerField(default=0, blank=True)
    leechers = models.IntegerField(default=0, blank=True)
    completed = models.IntegerField(default=0, blank=True)

    def __unicode__(self):
        return ' '.join((self.info_hash,str(self.query_date)))

class Torrent(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User)
    groups = models.ManyToManyField(Group, blank=True)
    likes = models.IntegerField(default=0, blank=True)
    size = models.IntegerField()
    info_hash = models.CharField(max_length=40)
    date = models.DateTimeField(default=datetime.utcnow, blank=True)
    trackers = models.ManyToManyField(Tracker)
    
    def __unicode__(self):
        return self.name

class TorrentFile(models.Model):
    torrent = models.OneToOneField(Torrent, primary_key=True)
    name = models.CharField(max_length=200)
    data = models.BinaryField()

    def __unicode__(self):
        return self.name
