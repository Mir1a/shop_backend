from django.core.management.base import BaseCommand

from ...homework import query


class Command(BaseCommand):
    help = 'Запуск задач'

    def handle(self, *args, **options):
        query.main()
