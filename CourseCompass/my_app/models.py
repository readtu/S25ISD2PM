from django.db import models

class DataEntry(models.Model):
    data_column = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data_column