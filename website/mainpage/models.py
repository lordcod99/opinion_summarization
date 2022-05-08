from django.db import models


class data(models.Model):
    id = models.AutoField(primary_key=True)
    input_data = models.TextField()
    summary = models.TextField()
