from django.db import models

from prochool.core.db.citizen import Citizen


# todo get fathers, get mothers, get others in manager
class Parent(Citizen):
    """Parent Model: Encapsulate Parent base information

    Type: is Father or Mother, ...
    students: related name in Student Model for Many to Many Relation
    base informations are encapsulated in Citizen Abstract Model
    """

    TYPE = (("f", "Father"), ("m", "Mother"), ("o", "Other"))
    type = models.CharField(max_length=1, choices=TYPE)
    profession = models.CharField(max_length=255)

    def __str__(self):
        return '{} {}'.format(self.last_name.upper(), self.first_name.title())
