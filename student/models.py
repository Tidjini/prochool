import black
from django.db import models

# Create your models here.


class Student(models.Model):
    """Student Model

    pk: is a code barre with EAN13
    """

    code_barre = models.CharField(max_length=13, primary=True)
