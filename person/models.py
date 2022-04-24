from django.db import models

# Create your models here.


TYPE = (
    (0, 'Education'),
    (1, 'Experience'),
    (2, 'Skills'),
    (3, 'Awards'),
)


class Tag(models.Model):
    tag = models.ImageField(upload_to='icon')

    def __repr__(self):
        return self.tag


class About(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='person')
    birth = models.DateField()
    live = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Resume(models.Model):
    start_finish = models.CharField(max_length=255)
    type = models.IntegerField(choices=TYPE)
    profession = models.CharField(max_length=255)
    academy = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icon')
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.profession
