from copy import deepcopy

from rest_framework import permissions

class DjangoModelPermissionWithGET(permissions.DjangoModelPermissions):

    def __init__(self):
        self.perms_map = deepcopy(self.perms_map)  # from EunChong's answer
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']