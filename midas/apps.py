from django.apps import AppConfig


class MidasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'midas'

    def ready(self) \
            -> None:
        import midas.signals