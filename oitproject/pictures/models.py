from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    cat_id = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name