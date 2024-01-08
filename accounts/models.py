from django.db import models
from django.contrib.auth.models import AbstractUser

class UserAccount(AbstractUser):
    email = models.EmailField(blank=False, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.username

    def to_dict(self) -> dict[str, str]:
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
