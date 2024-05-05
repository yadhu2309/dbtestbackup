from django.apps import AppConfig


class BackupappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backupapp'
    def ready(self) -> None:
        from .scheduler import scheduler
        scheduler.start()
