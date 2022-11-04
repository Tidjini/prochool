from django.conf import settings
from django.db import models

from prochool.core.db.citizen import Citizen

# Create your models here.


class Teacher(Citizen):
    '''Teacher: Store teacher informations

    Teacher is user of application, and he has authentication creadentials
    '''

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE
    )
