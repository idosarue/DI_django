from django.db import models



DEMO_CHOICES =(
    ("1", "actions"),
    ("2", "celebrities"),
    ("3", "decades"),
    ("4", "emotions"),
    ("5", "sports"),
    ("6", "food & drink"),
    ("7", "anime"),
    ("8", "memes"),
    ("9", "movies"),
    ("10", "tv"),
)

class Gif(models.Model):
    title = models.CharField(max_length=80)
    url = models.URLField(unique=True)
    uploader_name = models.CharField(max_length=50)
    categories = models.CharField(max_length=20,choices=DEMO_CHOICES, default='asd')
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    gifs = models.ManyToManyField(Gif)

    class Meta:
        verbose_name_plural = 'Categories'





