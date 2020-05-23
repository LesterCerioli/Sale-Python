from django.apps import AppConfig
from watson import search as watson

class CatalogConfig(AppConfig):
    name = 'catalog'
    verbose_name = 'Catálogo'

    def ready(self):
        """ para funcionar o watson """
        Product = self.get_model('Product')
        watson.register(Product)


    
