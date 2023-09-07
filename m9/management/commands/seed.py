from django.core.management.base import BaseCommand
from m9.models import MagicSquare
from ._private import generate


class Command(BaseCommand):
    help = "Generates the 9 x 9 pan-magic squares and seeds the database."

    def add_arguments(self, parser):
        parser.add_argument('-s', '--symmetric_only', action='store_true',
                            help="Keep symmetric magic squares only.")

    def handle(self, *args, **options):
        for data in generate(s=options["symmetric_only"]):
            MagicSquare.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded.'))
