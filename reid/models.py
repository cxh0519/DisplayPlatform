from django.db import models


class ReidImage(models.Model):
    unicode = models.CharField(max_length=50, primary_key=True)
    image = models.ImageField(upload_to='reid', null=True)

    def __str__(self):
        return self.unicode
