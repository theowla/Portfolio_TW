from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=100, default="Untitled Project")  # Default project name
    description = models.TextField(blank=True, null=True)  # Optional field
    image = models.ImageField(upload_to='images/')  # Field for the image

    def __str__(self):
        return self.description 
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name="images", on_delete=models.CASCADE)  # Link to the Post model
    image = models.ImageField(upload_to='post_images/')  # Store images in /media/post_images/

    def __str__(self):
        return f"Image for Post {self.id}"  # Return a description like "Image for Post 1"