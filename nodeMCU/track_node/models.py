from django.db import models

class Node_spi(models.Model):
    NODE = models.TextField()
    MAC = models.TextField()
    RSSI = models.TextField()
    TIME = models.TextField()
    DIST = models.TextField()
