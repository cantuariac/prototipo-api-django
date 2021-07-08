# from apps.api.models import Registro
from django.contrib.auth import get_user_model

User = get_user_model()

user = User.objects.create_user('caio', password='1234')
user.save()

# r = Registro(usuario=user, descricao='Registro feito por '+user.username)
# r.save()