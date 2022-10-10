from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Vechicles,VecicleImage,Wishlist,Sales



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password"]
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class VechicleSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Vechicles
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        return Vechicles.objects.create(**validated_data,user=user)

class ImageSerilaizer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    vechicle=serializers.CharField(read_only=True)
    class Meta:
        model=VecicleImage
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        vechicle=self.context.get("vechicle")
        return VecicleImage.objects.create(**validated_data,user=user,vechicle=vechicle)

class WishlistSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    vechicle=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    class Meta:
        model=Wishlist
        fields="__all__"
    def create(self,validated_data):
        user=self.context.get("user")
        vechicle=self.context.get("vechicles")
        return Wishlist.objects.create(**validated_data,user=user,vechicle=vechicle)