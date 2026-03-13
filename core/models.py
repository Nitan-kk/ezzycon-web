from django.db import models # db nahi, models import hota hai

class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='projects/') # Abhi ke liye ise comment kar de agar library install nahi hai
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title