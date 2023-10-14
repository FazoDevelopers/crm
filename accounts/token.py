from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from rest_framework_simplejwt.serializers import Dict,Any,api_settings,update_last_login,TokenObtainSerializer


class CustomTokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data['type_user'] = self.user.type_user
        

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]