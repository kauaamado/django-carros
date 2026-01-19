from django.contrib import admin
from cars.models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    
    # Colunas consultadas na busca
    search_fields = ('model', 'brand')

# Registra no site admin
admin.site.register(Car, CarAdmin)