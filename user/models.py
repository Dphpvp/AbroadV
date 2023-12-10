from django.db import models


class User(models.Model):
    gender_options = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    gender = models.CharField(choices=gender_options, max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile = models.ImageField(upload_to='profiles/', null=True)

    # auto_now_add = True folosit pt a va stoca data si ora in momentul in care s-a creat userul
    # auto_now = True folosit pt orice modificare sa salveze data si ora cand s-a modificat userul

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
