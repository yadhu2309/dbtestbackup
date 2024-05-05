from typing import Any
from backupapp.models import Blog
from django.core.management import  BaseCommand

class Command(BaseCommand):
    help = "Read Blog data"

    def handle(self, *args: Any, **options: Any) -> str | None:
        print(f'Starting to read blogs...')
        blog = Blog.objects.all()
        print(blog)