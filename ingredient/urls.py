from rest_framework import routers
from . import views


router = routers.DefaultRouter()

router.register("", views.IngredientViewset, basename="ingredient")

urlpatterns = router.urls