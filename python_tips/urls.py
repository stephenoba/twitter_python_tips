from django.urls import path

from . import views

app_name = "python_tips"

urlpatterns = [
    path("", views.index_view, name="index"),
]
