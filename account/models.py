from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length = 50)


class Users(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return f"Name:{self.name}, Age:{self.age}, Email:{self.email}, Role:{self.role.name}"

