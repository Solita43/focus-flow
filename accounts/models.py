from django.db import models
from django.contrib.auth.models import AbstractUser

class UserAccount(AbstractUser):
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
