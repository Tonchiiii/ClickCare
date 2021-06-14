from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Record(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    diagnosis = models.TextField()
    severity_score = models.TextField()
    def __str__(self):
        return self.user