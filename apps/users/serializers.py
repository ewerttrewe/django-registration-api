from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UsernameResetConfirmSerializer

User = get_user_model()

# pamietaj zeby to dokonczyc mialem rozpoczac pisac serailizer dla profilu
# dokoncyzc ten serializer czyli wytypowac pola
# dopisac metody jezeli jakiekolwiek potrzebuje nie mysallem o tym
# dokonczyc autentykacje z djosererm i simpleJWT zsrobic sygnaly dla profilu
# zrobic system logowania
# zrobic model ticketu i commitowac kod.
# djoser endpointy i urle 

class UserSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField(source='profile.profile_photo')
    gender = serializers.CharField(source='profile.gender')
    role = serializers.SerializerMethodField(source='profile.role')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
    
    def get_first_name(self, obj):
        return obj.first_name.title()
    
    def get_last_name(self, obj):
        return obj.last_name.title()

    def get_role(self, obj):
        return obj.role


class CreateUserSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']


