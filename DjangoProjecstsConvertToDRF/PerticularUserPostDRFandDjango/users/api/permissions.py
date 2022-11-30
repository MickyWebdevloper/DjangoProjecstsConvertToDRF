# from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.permissions import BasePermission


class IsPostOwner(BasePermission):
    has_perms = ['PUT', 'GET','DELETE']
    # has_perms = ['GET']
    message = 'Your do not have permission'

    def has_permission(self, request, view):
        if request.method in self.has_perms:
            return True

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True

        # if request.method in self.has_perms:
        #     return True
            # # Instance must have an attribute named `owner`.
        # return obj.author == request.user
