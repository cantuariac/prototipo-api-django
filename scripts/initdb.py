# from apps.api.models import Registro
from prototipo.apps.api.models import Profile, Registro
from django.contrib.auth import get_user_model
from faker import Faker
import random

User = get_user_model()


faker: Faker = Faker(locale='pt-br')

user = User.objects.create_user('admin', password='1q2w')
user.is_superuser = True
user.is_staff = True
user.save()

user = User.objects.create_user('caio', password='1234')
user.save()
Profile(usuario=user, nome='Caio', sobrenome='Cantuária',
        admissao=faker.past_date('-300d')).save()

r = Registro(usuario=user, descricao='Registro feito por '+user.username)
r.save()


for i in range(5):
    nome = faker.first_name()
    sobrenome = faker.last_name()

    user = User.objects.create_user((nome+sobrenome).lower(), password='1234')
    user.save()
    Profile(usuario=user, nome=nome, sobrenome=sobrenome,
            admissao=faker.past_date('-300d')).save()


users = list(User.objects.all())

for i in range(30):
    Registro(usuario=users[random.randint(0, len(users)-1)], descricao=faker.catch_phrase()+', '+faker.address()).save()
