from django.apps import AppConfig


class ShortConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'short'

# signals
class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
