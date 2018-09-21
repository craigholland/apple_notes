from tastypie.resources import ModelResource
from api.models import Note
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie import fields
from django.contrib.auth.models import User

from api.logger import Logger
from django.conf.urls import url, include



class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login', 'resource_uri', 'id']
        allowed_methods = ['get']

class NoteResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
