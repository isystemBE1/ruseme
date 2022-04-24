from django.db import models

# Create your models here.


class Services(models.Model):
    icon = models.ImageField(upload_to='icon')
    profession = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.profession


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Projects(models.Model):
    image = models.ImageField(upload_to='projects')
    category = models.ManyToManyField(Category, blank=True)
    profession = models.CharField(max_length=255)

    def __str__(self):
        return self.profession
