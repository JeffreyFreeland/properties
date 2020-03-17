from django.db import models
from django.core.validators import MinLengthValidator


class Property(models.Model):
    address = models.CharField(max_length=200, validators=[MinLengthValidator(1)])
    city = models.CharField(max_length=50, validators=[MinLengthValidator(1)])
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip = models.CharField(max_length=10, validators=[MinLengthValidator(5)])

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}, {self.zip}"
