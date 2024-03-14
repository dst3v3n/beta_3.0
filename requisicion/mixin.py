from django.contrib.auth.mixins import PermissionRequiredMixin
from admins.models import Myuser
from django.shortcuts import redirect

class EmailVerificadoMixin(PermissionRequiredMixin):

    permission_required = 'correo_electronico_verificado'
    login_url = '/curriculum/create/hoja/'

    def handle_no_permission(self):
        return redirect("verify-email")

    def has_permission(self):
        user = self.request.user
        if not user.is_active or not user.email_is_verified:
            return False
        return super().has_permission()
