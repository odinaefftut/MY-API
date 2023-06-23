import random
from django.core.management.base import BaseCommand
from apps.models import TestModel

class Command(BaseCommand):
    help = 'Creates random TestModel objects'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of TestModel objects to create')

    def handle(self, *args, **options):
        total = options['total']
        for _ in range(total):
            title = f'Test Object {random.randint(1, 100)}'
            description = f'Description for {title}'
            image = 'path/to/image.png'  # Specify the path to the image file here
            TestModel.objects.create(title=title, description=description, image=image)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} TestModel objects.'))
