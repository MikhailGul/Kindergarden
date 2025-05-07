from django.core.management.base import BaseCommand
from children.models import Child

class Command(BaseCommand):
    help = 'Create default galleries for existing children'

    def handle(self, *args, **options):
        for child in Child.objects.filter(status='approved'):
            if not child.photos.exists():
                child.create_default_gallery()
                self.stdout.write(f'Created gallery for {child}')