from django.shortcuts import render
from api.models import Vechicles,User,VecicleImage,Wishlist
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework import authentication,permissions
from api.serializer import UserSerializer,VechicleSerializer,ImageSerilaizer,WishlistSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
#localhost:8000/user/signup/
class UsersignupView(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

#localhost:8000/bikes/
class VechicleView(ModelViewSet):
    def list(self, request, *args, **kwargs):
      all_bikes=Vechicles.objects.all()
      serializer=VechicleSerializer(all_bikes,many=True)
      return Response(data=serializer.data)

# localhost:8000/bikes/{id}
    def retrieve(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        bike=Vechicles.objects.get(id=id)
        serializer=VechicleSerializer(bike,many=False)
        return Response(data=serializer.data)

#localhost:8000/bikes/add_bike
    @action(methods=["POST"],detail=False)
    def add_bike(self,request,*args,**kwargs):
       user=request.user
       serializer=VechicleSerializer(data=request.data,context={"user":user})
       if serializer.is_valid():
           serializer.save()
           return Response(data=serializer.data)
       else:
           return Response(data=serializer.errors)
#localhost:8000/bikes/{id}/add_image
    @action(methods=["POST"],detail=True)
    def add_image(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        user=request.user
        bike=Vechicles.objects.get(id=id)
        serializer=ImageSerilaizer(data=request.data,context={"user":user,"vechicle":bike})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
#localhost:8000/bikes/{id}/get_images
    @action(methods=["GET"],detail=True)
    def get_image(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        bike=Vechicles.objects.get(id=id)
        images=bike.vecicleimage_set.all()
        serializer=ImageSerilaizer(images,many=True)
        return Response(data=serializer.data)
#localhost:8000/bikes/{id}/add_to_wishlist/
    @action(methods=["POST"],detail=True)
    def add_to_wishlist(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        bike=Vechicles.objects.get(id=id)
        uid=request.user
        serializer=WishlistSerializer(data=request.data,context={"user":uid,"vechicles":bike})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

#localhost:8000/wishlist/
class WishlistView(ModelViewSet):
    serializer_class =WishlistSerializer
    queryset = Wishlist.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)