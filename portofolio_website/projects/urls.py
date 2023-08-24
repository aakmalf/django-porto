from django.urls import path
from .views import ProjectsListView,CategoryProjectsListView

app_name = "projects"

urlpatterns = [
    path("<int:page>", ProjectsListView.as_view(), name="index"),
    # path("category/<str:category>", CategoryProjectsListView.as_view(), name="category")
    path("category/<str:category>/<int:page>", CategoryProjectsListView.as_view(), name="category")
]