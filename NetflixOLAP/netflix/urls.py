from rest_framework.routers import SimpleRouter
from .views import UserDemographicsViewSet, AverageHoursPerUserViewSet, PopularDirectorViewSet, PopularShowViewSet, PopularActorViewSet, PopularGenreViewSet, ContentRecommendationViewSet, UserSatisfactionViewSet


router = SimpleRouter()

router.register("UserDemographics", UserDemographicsViewSet)
router.register("AverageHoursPerUser", AverageHoursPerUserViewSet)
router.register("PopularDirector", PopularDirectorViewSet)
router.register("PopularShow", PopularShowViewSet)
router.register("PopularActor", PopularActorViewSet)
router.register("PopularGenre", PopularGenreViewSet)
router.register("ContentRecommendation", ContentRecommendationViewSet)
router.register("UserSatisfaction", UserSatisfactionViewSet)

urlpatterns = router.urls
