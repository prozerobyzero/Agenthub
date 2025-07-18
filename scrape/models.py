from django.db import models

class Scrape(models.Model):
    weblink = models.URLField(max_length=500)
    data = models.TextField()
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.weblink
