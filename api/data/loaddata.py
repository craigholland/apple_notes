from api.data import default_data as data
from django.contrib.auth.models import User

def load():
    for user in data.USERS:
        new_user = User(username=user['username'])
        if 'first_name' in user.keys():
            new_user.first_name = user['first_name']

        if 'last_name' in user.keys():
            new_user.last_name = user['last_name']
        new_user.set_password(user['password'])
        new_user.save()




