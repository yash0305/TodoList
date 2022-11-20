from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Todo(models.Model):
    CHOICES = (
        ('open', 'OPEN'),
        ('working', 'WORKING'),
        ('done', 'DONE'),
        ('overdue' ,'OVERDUE'),
    )
    Timestamp = models.DateTimeField(auto_now_add=True)
    Title = models.CharField(max_length=100)
    Description = models.TextField(max_length=1000)
    Due_Date = models.DateField(blank=True, null=True)
    Tag = models.ManyToManyField(Tag, blank=True, null=True)
    Status = models.CharField(max_length=20,choices=CHOICES, default='open')

    
    def __str__(self):
        return self.Title