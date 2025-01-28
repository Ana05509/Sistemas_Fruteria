from django.apps import AppConfig

class FrutasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'frutas'

    def ready(self):
        # Aquí se pueden importar señales u otras configuraciones, si es necesario
        pass



