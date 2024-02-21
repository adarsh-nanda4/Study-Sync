from django.db import models

# Create your models here.
class Notice(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=10000)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} - {self.id}"