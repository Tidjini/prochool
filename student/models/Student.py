from django.db import models

from student.models.Citizen import Citizen
from student.models.Establishment import Establishment
from student.models.Parent import Parent

# Create your models here.


class Student(Citizen):
    """Student Model, ordinare student model

    pk: is a code barre with EAN13
    defauts fields are contained in Citizen like:
        - first_name, last_name, phone, birthdate
    """

    SEX_TYPE = (("m", "Male"), ("f", "Female"))
    YEARS_OF_STUDY = (("1", "1st Year"), ("2", "2nd Year"), ("3", "3rd Year"))
    LEVELS_OF_STUDY = (
        ("vl", "Very Low"),
        ("l", "Low"),
        ("a", "Avrage"),
        ("g", "Good"),
        ("e", "Excelent"),
    )
    BRANCHES = (("math", "Math"), ("science", "Science"), ("science", "Science"))

    barre_code = models.CharField(max_length=13, primary_key=True)
    sex = models.CharField(max_length=1, choices=SEX_TYPE)
    branch = models.CharField(max_length=30, choices=BRANCHES)
    year_of_study = models.CharField(max_length=1, choices=YEARS_OF_STUDY)
    level_of_study = models.CharField(max_length=2, choices=LEVELS_OF_STUDY)

    parents = models.ManyToManyField(Parent)

    establishment = models.ForeignKey(
        Establishment, on_delete=models.SET_NULL, related_name="students", null=True
    )

    observation = models.CharField(max_length=255)
