from django.db.models import Q
from users.models import Profile
from django.forms import ValidationError
from django.contrib.auth.models import User
from rest_framework.serializers import (
    ModelSerializer,
    CharField
)

class UserDetail(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']

class ProfileSerializer(ModelSerializer):
    user = UserDetail()

    class Meta:
        model = Profile
        fields = ['id', 'user','image']
    

# from django.contrib.auth import authenticate


class UserCreateSerializer(ModelSerializer):
    password2 = CharField(label='Confirm Password')

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'password2'
        ]
        extra_kwargs = {'password2':
                        {'write_only': True}
                        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            # password=validated_data['password']
        )
        user.set_password(user.password)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_email(self, data):
        email_qs = User.objects.filter(email=data)
        if email_qs.exists():
            raise ValidationError('This Email is already exists')
        return data

    # def validate_empty_values(self, data):
    #     password = data.get_initial()
    #     password2 = data
    #     return data

    def validate(self, attrs):
        username = attrs['username']
        email = attrs['email']
        password = attrs['password']

        if (not email) or (not username) or (not password):
            raise ValidationError('All fields are required to Registered')

        return attrs


class UserLoginSerializer(ModelSerializer):
    # email = CharField(null=True, blank=True)
    password = CharField(required=False)

    class Meta:
        model = User
        fields = [
            'email', 'password'
        ]

    def validate(self, attrs):
        user_obj = None
        email = attrs.get('email', None)
        password = attrs.get('password', None)
        print('email ----------->', email)
        print('password ----------->', password)
        if not email and not password:
            raise ValidationError('Email and Password required to login ')

        user = User.objects.filter(
            Q(email=email) |
            Q(password=password)
        ).distinct()

        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        print(user)

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('This email is not valid')

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError(
                    'Incorrect Credetianils please check your data')
        return attrs
