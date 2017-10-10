from rest_framework import serializers
from .models import UserDemographics, AverageHoursPerUser, PopularDirector, PopularShow, PopularActor, PopularGenre, ContentRecommendation, UserSatisfaction

class UserDemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDemographics
        fields = ('user_name', 'state')


class AverageHoursPerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AverageHoursPerUser
        fields = ('user_name', 'content_id', 'stream_length')


class PopularDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularDirector
        fields = ('director_name', 'count')


class PopularShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularShow
        fields = ('title', 'count')


class PopularActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularActor
        fields = ('cast_name', 'count')


class PopularGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularGenre
        fields = ('genre_desc', 'count')


class ContentRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentRecommendation
        fields = ('user_name', 'genre_desc', 'genre_count', 'cast_name', 'cast_count', 'director_name', 'director_count')


class UserSatisfactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSatisfaction
        fields = ('user_name', 'state', 'user_country', 'video_quality', 'audio_quality', 'subtitle_quality', 'content_id')
