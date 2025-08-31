from django.urls import path
from .views import dashboard_overview, upcoming_tasks

urlpatterns = [
    path('overview/', dashboard_overview, name='dashboard-overview'),
    path('upcoming-tasks/', upcoming_tasks, name='upcoming-tasks'),
]