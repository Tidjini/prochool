from django.conf import settings
from django.db import models

from core.db.Citizen import Citizen

# Create your models here.


class Teacher(Citizen):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE
    )
