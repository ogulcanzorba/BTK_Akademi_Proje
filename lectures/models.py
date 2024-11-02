from django.db import models
from django.utils.text import slugify


class Lectures(models.Model):
    lecture_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=False, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.lecture_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.lecture_name
