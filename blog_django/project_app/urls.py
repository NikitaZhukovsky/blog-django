from django.urls import path
from project_app.views import some_views


urlpatterns = [
    path('some-view/', some_views)
]