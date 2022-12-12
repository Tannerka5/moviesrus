from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.SmallIntegerField()
    rating = models.ForeignKey(
        'Rating',
        on_delete=models.DO_NOTHING,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return self.title
    class Meta():
        db_table= "movie"

class Rating(models.Model):
    rating = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length= 100)

    def __str__(self):
        return self.rating
    class Meta():
        db_table= "rating"

class Category(models.Model):
    category = models.CharField(max_length=1, unique=True)
    description = models.CharField(max_length=20)

    def __str__(self):
        return self.category
    class Meta():
        db_table= "category"

