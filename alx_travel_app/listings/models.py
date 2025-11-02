from django.db import models

# Example model (you can extend later)
class ExampleModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
