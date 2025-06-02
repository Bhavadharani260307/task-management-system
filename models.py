from django.db import models
from datetime import date
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField(default=date.today)  # ✅ Set default here
    is_completed = models.BooleanField(default=False)
