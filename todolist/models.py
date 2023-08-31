from django.db import models


class TodoList(models.Model):
    note = models.CharField(max_length=255)
