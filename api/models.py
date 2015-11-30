from django.contrib.auth.models import Permission
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.utils.translation import ugettext_lazy as _

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

class Connection(models.Model):
    port = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    dateTime = models.DateField()
    unitId = models.IntegerField(null=True)
    permissions = models.ManyToManyField(Permission, verbose_name=_('permissions'), blank=True)

class Event(models.Model):
    port = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    unitId = models.IntegerField()
    dateTime = models.DateField()

class Monitoring(models.Model):
    unitId = models.IntegerField()
    beginTime = models.DateField()
    endTime = models.DateField()
    type = models.CharField(max_length=255)
    min = models.CharField(max_length=255)
    max = models.CharField(max_length=255)
    sum = models.CharField(max_length=255)

class Position(models.Model):
    unitId = models.IntegerField()
    rDx = models.CharField(max_length=255)
    rDy = models.CharField(max_length=255)
    speed = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    numSattellites = models.IntegerField()
    hdop = models.IntegerField()
    quality = models.CharField(max_length=255)
    dateTime = models.DateField()

