import uuid
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, default='', unique=True)
    email = models.EmailField(default='', unique=True)
    password = models.CharField(max_length=100, default='')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f'Name: {self.name} | E-mail: {self.email}'
