from django.db import models


class UserHistory(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


from django.db import models

# Create your models here.
