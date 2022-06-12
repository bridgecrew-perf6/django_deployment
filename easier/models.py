from django.db import models

class TestMessage(models.Model):
    test_message = models.CharField(max_length=250)
