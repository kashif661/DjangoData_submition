from django.db import models

class Submit(models.Model):
    Uname = models.CharField(max_length=50)
    email = models.CharField(max_length=60)


