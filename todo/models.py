import datetime

from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
