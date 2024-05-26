from django.apps import AppConfig


class SocialNetworkAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'song_app'

    def ready(self):
        import song_app.signals