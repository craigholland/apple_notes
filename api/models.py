from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def username(self):
        return self.user.username

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    def __str__(self):
        return '{0} {1}'.format(self.title, self.body)

    def get(self):
        pass

    
