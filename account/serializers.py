from rest_framework import serializers
from .models import CustomUser, Blog


class CustomUserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email','date_joined','location', 'bio','followers', 'following', 'company','linkedin', 'github','avatar')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            avatar=validated_data['avatar'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class BlogSerializers(serializers.ModelSerializer):
    avatar = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Blog
        fields = ('title','location','description','followers','created_at','avatar','user')
