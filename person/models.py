from django.db import models
from main.models import Category

TYPE = (
    (0, 'Education'),
    (1, 'Experience'),
    (2, 'Skills'),
    (3, 'Awards'),
)


class Partner(models.Model):
    image = models.ImageField(upload_to='icon')

    def __str__(self):
        return self.image.name


class About(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='person')
    birth = models.DateField()
    live = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Resume(models.Model):
    start_finish = models.CharField(max_length=255, null=True, blank=True)
    type = models.IntegerField(choices=TYPE)
    profession = models.CharField(max_length=255, null=True, blank=True)
    academy = models.CharField(max_length=255, null=True, blank=True)
    icon = models.ImageField(upload_to='icon', null=True, blank=True)
    is_skill = models.BooleanField(default=False)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        if self.profession:
            return self.profession
        return 'Skill'


class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    percent = models.IntegerField()

    def __str__(self):
        return self.title


class Projects(models.Model):
    image = models.ImageField(upload_to='projects')
    category = models.ManyToManyField(Category, blank=True)
    link = models.URLField()
    profession = models.CharField(max_length=255)

    def __str__(self):
        return self.profession