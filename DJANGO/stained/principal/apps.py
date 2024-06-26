from django.apps import AppConfig


class PrincipalConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "principal"

    def ready(sefl):
        import principal.signals
