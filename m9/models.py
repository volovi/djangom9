from django.contrib.postgres.fields import ArrayField
from django.db.models import Model, CharField, IntegerField


class MagicSquare(Model):
    values = ArrayField(ArrayField(IntegerField(), size=9), size=9)
    hint = CharField(max_length=127, blank=True)

    def __str__(self):
        return self.hint
