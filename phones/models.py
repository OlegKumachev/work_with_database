from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(max_length=255)
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name}, {self.price}, {self.image}, {self.release_date}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
