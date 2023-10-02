from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from projects.models import projects    

# Create your views here

class HomeView(ListView):
    model = projects
    template_name = "home/index.html"
    context_object_name = "list_projects"
    ordering = ['-published']

    def get_queryset(self):
        return self.model.objects.order_by('-published')[:2]
    



    

