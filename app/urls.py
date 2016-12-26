from rest_framework.routers import DefaultRouter
from app.translation.views import TranslationViewSet


router = DefaultRouter()
router.register(prefix="translations", viewset=TranslationViewSet)

urlpatterns = router.urls
