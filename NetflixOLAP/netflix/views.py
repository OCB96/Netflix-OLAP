from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import UserDemographics, AverageHoursPerUser, PopularDirector, PopularShow, PopularActor, PopularGenre, ContentRecommendation, UserSatisfaction
from .serializers import UserDemographicsSerializer, AverageHoursPerUserSerializer, PopularDirectorSerializer, PopularShowSerializer, PopularActorSerializer, PopularGenreSerializer, ContentRecommendationSerializer, UserSatisfactionSerializer

class UserDemographicsViewSet(ModelViewSet):
    serializer_class = UserDemographicsSerializer
    queryset = UserDemographics.objects.all()

class AverageHoursPerUserViewSet(ModelViewSet):
    serializer_class = AverageHoursPerUserSerializer
    queryset = AverageHoursPerUser.objects.all()

class PopularDirectorViewSet(ModelViewSet):
    serializer_class = PopularDirectorSerializer
    queryset = PopularDirector.objects.all()

class PopularShowViewSet(ModelViewSet):
    serializer_class = PopularShowSerializer
    queryset = PopularShow.objects.all()

class PopularActorViewSet(ModelViewSet):
    serializer_class = PopularActorSerializer
    queryset = PopularActor.objects.all()

class PopularGenreViewSet(ModelViewSet):
    serializer_class = PopularGenreSerializer
    queryset = PopularGenre.objects.all()

class ContentRecommendationViewSet(ModelViewSet):
    serializer_class = ContentRecommendationSerializer
    queryset = ContentRecommendation.objects.all()

class UserSatisfactionViewSet(ModelViewSet):
    serializer_class = UserSatisfactionSerializer
    queryset = UserSatisfaction.objects.all()
