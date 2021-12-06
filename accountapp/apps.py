from django.apps import AppConfig


class AccountappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accountapp'

# signal

# class UsersConfig(AppConfig):
#     name = 'users'
#
#     def ready(self):
#         import users.signals
