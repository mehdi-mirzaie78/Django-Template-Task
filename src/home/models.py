from django.db import models
from django.utils.translation import gettext_lazy as _


class Passenger(models.Model):
    class Meta:
        ordering = ("-id",)

    class PClassChoices(models.IntegerChoices):
        FIRST = 1
        SECOND = 2
        THIRD = 3

    class SexChoices(models.TextChoices):
        MALE = "male", _("Male")
        FEMALE = "female", _("Female")

    class EmbarkedChoices(models.TextChoices):
        CHERBOURG = "C", _("Cherborg")
        QUEENTOWN = "Q", _("Queentown")
        SOUTHAMPTON = "S", _("Southampton")

    survived = models.BooleanField(default=False, verbose_name=_("Survived"))
    pclass = models.PositiveSmallIntegerField(verbose_name=_("Passenger Class"), choices=PClassChoices)
    name = models.CharField(max_length=120, verbose_name=_("Name"))
    sex = models.CharField(max_length=20, verbose_name=_("Sex"), choices=SexChoices)
    age = models.FloatField(verbose_name=_("Age"), null=True, blank=True)
    sibsp = models.PositiveSmallIntegerField(verbose_name=_("Passenger Siblings Count"))
    parch = models.PositiveSmallIntegerField(verbose_name=_("Parent Child Count"))
    ticket = models.CharField(max_length=120, verbose_name=_("Ticket Code"))
    fare = models.DecimalField(max_digits=8, decimal_places=4, verbose_name=_("Fare"))
    cabin = models.CharField(max_length=100, verbose_name=_("Cabin"), null=True, blank=True)
    embarked = models.CharField(max_length=20, verbose_name=_("Embarked"), choices=EmbarkedChoices)

    def __str__(self):
        return f'ID: {self.pk} - {self.name}'
