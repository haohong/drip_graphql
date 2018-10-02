from django.apps import AppConfig


class PositionsConfig(AppConfig):
    name = 'positions'

    def ready(self):
        from .store import store

        # Import data from csv files
        store.load_all()
