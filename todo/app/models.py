from django.db import models
from django.core.exceptions import ValidationError
import datetime

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
    Tag = models.ManyToManyField(Tag, blank=True)
    Status = models.CharField(max_length=20,choices=CHOICES, default='open')

    def isDueDateNotPast(self):
        timeStamp = datetime.date.today()
        if self.Due_Date < timeStamp:
            return True
        else:
            return False

    def clean(self):
        if self.isDueDateNotPast():
            raise ValidationError('Only current date and future dates are allowed') 

    def get_tags(self):
        return ",\n".join([p.name for p in self.Tag.all()])       

