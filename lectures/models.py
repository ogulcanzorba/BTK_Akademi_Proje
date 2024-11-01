from django.db import models

class Lectures(models.Model):
    lecture_name = models.CharField(max_length=100)