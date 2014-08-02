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


class Torrent(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User)
    groups = models.ManyToManyField(Group)
    likes = models.IntegerField()
    size = models.IntegerField()
    info_hash = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.utcnow, blank=True)
    seeders = models.IntegerField()
    leechers = models.IntegerField()
    
    def __unicode__(self):
        return self.name

