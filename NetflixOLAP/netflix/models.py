from django.db import models

# Create your models here

class UserDemographics(models.Model):
    """
    Joins User Table and Zip table on zip_id to check which states most users are from
    Maybe used to focus promotion in particular locations
    """
    user_name = models.CharField(max_length=225)
    state = models.CharField(max_length=225)

class AverageHoursPerUser(models.Model):
    """
    Joins User, User Rentals and Rentals Tables on rental_id and user_id to find video streaming records for each user.
    An aggregate is taken per user across the number of rentals the user has.
    """
    user_name = models.CharField(max_length=225)
    content_id = models.IntegerField()
    stream_length = models.IntegerField()

class PopularDirector(models.Model):
    """
    Joins Rentals table and Content table on content_id, select director_id, then pull data from director table.
    Check frequency of a particular director.
    """
    director_name = models.CharField(max_length=225)
    count = models.IntegerField()

class PopularShow(models.Model):
    """
    Joins Rentals table and Content table on content_id, select title.
    Check frequency of a particular title.
    """
    title = models.CharField(max_length=225)
    count = models.IntegerField()

class PopularActor(models.Model):
    """
    Joins Rentals table and Content table on content_id, select cast_id, then pull data from cast table.
    Check frequency of a particular actor.
    """
    cast_name = models.CharField(max_length=225)
    count = models.IntegerField()

class PopularGenre(models.Model):
    """
    Joins Rentals table and Content table on content_id, select genre_id, then pull data from genre table.
    Check frequency of a particular genre.
    """
    genre_desc = models.CharField(max_length=225)
    count = models.IntegerField()

class ContentRecommendation(models.Model):
    """
    Joins User, User Rentals, Rentals and Content tables, to find out most watched Genre/Actor/Director for each user
    by checking the respective frequencies. Later, similar users based on the count
    can be recommended content from each other's rental lists.
    """
    user_name = models.CharField(max_length=225)
    genre_desc = models.CharField(max_length=225)
    genre_count = models.IntegerField()
    cast_name = models.CharField(max_length=225)
    cast_count = models.IntegerField()
    director_name = models.CharField(max_length=225)
    director_count = models.IntegerField()

class UserSatisfaction(models.Model):
    """
    https://npv.netflix.com/what-is-the-npv-program
    Joins User table and Ratings table to judge user satisfaction is consistent globally or not.
    Helps to improve in areas where satisfaction is minimal
    """
    user_name = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    user_country = models.CharField(max_length=225)
    video_quality = models.IntegerField()
    audio_quality = models.IntegerField()
    subtitle_quality = models.IntegerField(max_length=10)
    content_id = models.IntegerField()

# class UserLifetimeValue(models.Model):
#     """
#
#     """
