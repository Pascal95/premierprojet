from rest_framework import routers
from . import views


router = routers.DefaultRouter()

router.register("", views.RecetteViewSet, basename="recette")

urlpatterns = router.urls