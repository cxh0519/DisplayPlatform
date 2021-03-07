from django.db import models


class DetectionImage(models.Model):
    unicode = models.CharField(max_length=50, primary_key=True)
    image = models.ImageField(upload_to='detection', null=True)

    def __str__(self):
        return self.unicode
