from django.urls import path
from .views import TemplateView

app_name = "home"

urlpatterns = [
    path("", TemplateView.as_view(), name="index")
]