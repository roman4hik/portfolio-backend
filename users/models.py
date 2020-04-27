from django.contrib.auth.models import AbstractUser
from django.db import models

from .roles import Roles


class User(AbstractUser):
    date_of_birthday = models.DateTimeField(null=True, blank=True)
    role = models.CharField(
        choices=Roles.choices(), default=Roles.AUTHOR.name, max_length=20
    )

    class Meta:
        db_table = "users"
