from django.db import models

class Project(models.Model):
    
    title = models.CharField(max_length=100)
    tech = models.CharField(max_length=100)
    description = models.TextField()
  
    def __str__(self):
        return f"{self.title} - {self.tech}"


class Image(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photos/")  

    def __str__(self):
        return f"Image for {self.project.title}"