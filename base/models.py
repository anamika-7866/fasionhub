from django.db import models
class MainFrame(models.Model):
    logo = models.CharField(max_length=300)  # Use CharField for max_length
    image = models.ImageField(upload_to="media/")  # Set a proper upload path

    def __str__(self):
        return f"MainFrame {self.id}"