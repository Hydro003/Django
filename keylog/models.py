from django.db import models

class KeystrokeLog(models.Model):
    key = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.key} at {self.timestamp}'
