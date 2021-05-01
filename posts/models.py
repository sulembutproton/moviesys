from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class post(models.Model):
    title = models.CharField(max_length=200, help_text="Type film title!")
    video = EmbedVideoField(verbose_name="Video", help_text="Type url name!")
    url = models.URLField(max_length = 200, help_text="Type url name!")
    id = models.AutoField
    #video = models.CharField(max_length=200, help_text="Type file name!")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})
