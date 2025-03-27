from django.db import models
from django.core.validators import RegexValidator
from django.db.models import Avg

class Restaurant(models.Model):
    slug = models.SlugField(
        unique=True,
        validators=[RegexValidator(regex=r'^[-a-zA-Z0-9_]+$')],
        editable=False
    )
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField(max_length=256, blank=True, null=True)
    image = models.ImageField(upload_to='restaurant_images/')
    rating = models.FloatField(null=True, blank=True, editable=False)

    def update_rating(self):
        avg_rating = self.reviews.aggregate(Avg('rating'))['rating__avg']
        self.rating = round(avg_rating or 0, 2)
        self.save(update_fields=['rating'])

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
