import django
import os



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ueser_role_managment.settings")
django.setup()


from account.models import Role, Users 

# Role.objects.create(name = 'admin')
# Role.objects.create(name = 'superuser')
# Role.objects.create(name = 'user_defolt')

# Users.objects.create(name = "Olecsandr", age = 29, email = "olecsandr@gmail.com", role = Role.objects.get( id = 1 ))
# Users.objects.create(name = "Olecsandr", age = 29, email = "olecsandr@gmail.com", role = Role.objects.get( id = 2))
# Users.objects.create(name = "Olecsandr", age = 29, email = "olecsandr@gmail.com", role = Role.objects.get( id = 3 ))

user_1 = Users.objects.get(id = 1)
print(user_1)