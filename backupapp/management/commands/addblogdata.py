from typing import Any
from django.core.management import BaseCommand
from backupapp.models import Blog

class Command(BaseCommand):
    help = "Add data to Blog"

    def handle(self, *args: Any, **options: Any) -> str | None:
        for i in range(10):
            Blog.objects.create(data=f"yadhu{i}")
        print('Data added')
