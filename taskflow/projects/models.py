from django.db import models
from users.models import User  # This should work now

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, related_name='owned_projects', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='projects')
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title