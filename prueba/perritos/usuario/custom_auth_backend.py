from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomAuthBackend(ModelBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

    def _get_user_session_key(self, request):
        return request.session.get('_auth_user_id')