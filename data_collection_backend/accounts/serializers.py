from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User
from organisations.serializers import MinimizedOrganisationSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "username",
            "is_superuser",
            "is_staff",
            "is_active",
            "account_status",
            "groups",
            "user_permissions",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
            "organisation": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
            "gender": {"required": True},
            "phone_number_1": {"required": True},
        }

class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "role",
            "username",
            "is_superuser",
            "is_staff",
            "is_active",
            "account_status",
        ]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["organisation"] = user.organisation_id
        token["username"] = user.username
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["role"] = user.role
        token["user_permission"] = (
            f"{[perm.codename for perm in user.user_permissions.all()]}"
        )

        return token


class RetrieveUserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "firstName",
            "lastName",
            "middleNames",
            "gender",
            "altEmail",
            "phone_number_1",
        ]
    
class PasswordVerifyAndChangeSerializer(serializers.Serializer):
        username = serializers.CharField(required=True)
        password = serializers.CharField(required=True)

class PasswordResetSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)


class AuditTrailUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "gender",
            "organisation",
        ]

class RetrieveUserSerializer(ModelSerializer):
    organisation = MinimizedOrganisationSerializer()

    class Meta:
        model = User
        fields = "__all__"

        extra_kwargs = {"password": {"write_only": True}}


class MinimizedUserSerializer(ModelSerializer):
    organisation = MinimizedOrganisationSerializer()

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "organisation"]

        extra_kwargs = {"password": {"write_only": True}}
