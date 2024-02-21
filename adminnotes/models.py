from django.db import models

# Create your models here.
class Notes(models.Model):
    DEPARTMENTS = [
        ('BCA','BCA'),
        ('MCA','MCA')
    ]
    SEM = [
        ('Sem 1', 'Sem 1'),
        ('Sem 2', 'Sem 2'),
        ('Sem 3', 'Sem 3'),
        ('Sem 4', 'Sem 4'),
        ('Sem 5', 'Sem 5'),
        ('Sem 6', 'Sem 6')
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    department = models.CharField(max_length=10, choices=DEPARTMENTS,default='BCA')
    sem = models.CharField(max_length=10, choices=SEM,default='Sem 1')
    content = models.TextField(max_length=10000)
    date = models.DateField(auto_now_add=True)
    files = models.FileField(upload_to='Notes', blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.id}"

