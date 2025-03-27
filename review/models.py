from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from restaurant.models import Restaurant

class Review(models.Model):
    slug = models.SlugField(
        unique=True,
        validators=[RegexValidator(regex=r'^[-a-zA-Z0-9_]+$')],
        editable=False
    )
    restaurant = models.ForeignKey(Restaurant, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(f"{self.name}-{self.restaurant.name}")
        super().save(*args, **kwargs)
        self.restaurant.update_rating()

    def delete(self, *args, **kwargs):
        restaurant = self.restaurant
        super().delete(*args, **kwargs)
        restaurant.update_rating()

    def __str__(self):
        return f'Review {self.name} for {self.restaurant.name}'
