from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50, default='deafult')
    price = models.BigIntegerField(default=0)
    image = models.CharField(max_length=200, default='deafult')
    release_date = models.CharField(max_length=50, default='deafult')
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(default='deafult')

    def __str__(self):
        return f'{self.name}, {self.price}, {self.release_date}, {self.lte_exists}, {self.slug}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
