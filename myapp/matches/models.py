from pathlib import Path
from django.db import models
from django.utils.html import mark_safe

# Create your models here.
BASE_DIR = Path(__file__).resolve().parent.parent


class Game(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField(upload_to=BASE_DIR/"public/images/games")

    def __str__(self):
        return self.name

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))
        return ""


class Match(models.Model):
    name = models.CharField(max_length=50)
    team1_name = models.CharField(max_length=50)
    team2_name = models.CharField(max_length=50)
    team1_image = models.FileField(upload_to=BASE_DIR/"public/images/teams")
    team2_image = models.FileField(upload_to=BASE_DIR/"public/images/teams")
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    start_time = models.DateTimeField()

    def __str__(self):
        return self.name

    @property
    def team1image_preview(self):
        if self.team1_image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.team1_image.url))
        return ""

    @property
    def team2image_preview(self):
        if self.team2_image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.team2_image.url))
        return ""

    class Meta:
        verbose_name_plural = 'Matches'
