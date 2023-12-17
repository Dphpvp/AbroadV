from django.db import models

from user.models import User

from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
