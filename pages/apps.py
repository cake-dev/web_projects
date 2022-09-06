from django.apps import AppConfig

# inherits traits of AppConfig to configure django app
class PagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pages"
