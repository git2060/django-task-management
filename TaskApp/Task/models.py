from django.db import models

# Create your models here.

# name (CharField, max length 150, required)
# description (TextField, optional)
# is_completed (BooleanField, default=False)
# due_date (DateField, optional)

class TaskModel(models.Model):
    name=models.CharField(max_length=150)
    description = models.TextField(null=True)
    is_completed=models.BooleanField(default=False)
    due_date = models.DateField(null=True)

    def __str__(self):
        return self.name
