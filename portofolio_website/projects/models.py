from django.db import models

# Create your models here.
# judul, description, link, list category, tanggal, updated data

class category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class projects(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=200)
    link = models.URLField()
    categories = models.ManyToManyField(category)
    published = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title
