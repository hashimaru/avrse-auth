from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth

from sde.models import System, Type

from .corporation import Corporation
from .alliance import Alliance


class Character(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    last_updated = models.DateTimeField(auto_now=True)

    # Extra details, these are default null
    token = models.ForeignKey(UserSocialAuth, null=True, default=None)
    owner = models.ForeignKey(User, null=True, default=None, related_name="characters")
    corp = models.ForeignKey(Corporation, null=True, default=None)
    alliance = models.ForeignKey(Alliance, null=True, default=None)

    wallet = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    system = models.ForeignKey(System, null=True, default=None)
    ship = models.ForeignKey(Type, null=True, default=None)

    fatigue_expire_date = models.DateTimeField(null=True, default=None)
    last_jump_date = models.DateTimeField(null=True, default=None)


    @staticmethod
    def get_or_create(id):
        from eveauth.esi import ESI

        db_char = Character.objects.filter(id=id)
        if len(db_char) == 0:
            api = ESI()
            char = api.get("/characters/%s/" % id)
            db_char = Character(
                id=id,
                name=char['name']
            )
            db_char.save()
        else:
            db_char = db_char[0]

        return db_char
