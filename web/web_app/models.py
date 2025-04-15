from django.db import models

class StatusModel(models.Model):
        name = models.CharField(max_length = 200)
        description = models.TextField()
        create_at = models.DateTimeField(auto_now_add = True)
        updated_at = models.DateTimeField(auto_now = True)