from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.views.generic import DetailView, TemplateView, ListView

from .models import projects

# Create your views here

class CategoryProjectsListView(ListView):
    model = projects
    template_name = "projects/projects_category.html"
    context_object_name = "list_projects"
    ordering = ['-published']
    paginate_by = 4

    def get_queryset(self):        
        self.queryset = self.model.objects.filter(categories__name=self.kwargs["category"])
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        from .models import category  # Import the Category model
        
        excluded_category_name = self.kwargs["category"]
        
        category_list = category.objects.exclude(name=excluded_category_name)
        
        context['category_list'] = category_list
        return context

class ProjectsListView(ListView):
    model = projects
    template_name = "projects/projects.html"
    context_object_name = "list_projects"
    ordering = ['-published']
    paginate_by = 4


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        from .models import category  # Import the Category model
        
        category_list = category.objects.all()  # Retrieve all categories
        
        context['category_list'] = category_list
        return context
    
  

