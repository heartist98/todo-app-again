from django.apps import AppConfig

class TodosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todos'
    label = 'todos_unique'  # Add unique label to prevent conflicts