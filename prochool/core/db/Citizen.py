from django.db import models


class Citizen(models.Model):
    """Citizen: Abstract Model containe:

    first & last name, phone, birthdate
    """

    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    birthdate = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return '{} {}'.format(self.last_name.upper(), self.first_name.title())

    @property
    def name(self):
        return '{} {}'.format(self.last_name.upper(), self.first_name.title())
