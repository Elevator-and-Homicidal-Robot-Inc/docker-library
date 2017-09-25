from django.db import models
from django.utils import timezone


class PageView(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
