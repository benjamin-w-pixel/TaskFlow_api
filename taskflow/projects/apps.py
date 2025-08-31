from django.apps import AppConfig

class ProjectsConfig(AppConfig):   # ✔ fixed
    default_auto_field = "django.db.models.BigAutoField"
    name = "projects"              # ✔ fixed
