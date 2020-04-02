from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=200)
    body=models.CharField(max_length=500)
    imglink=models.CharField(max_length=655)

    def __str__(self):
        return f"{self.title}  {self.body}  {self.imglink}"