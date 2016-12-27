from rest_framework.routers import DefaultRouter
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from app.translation.views import TranslationViewSet


router = DefaultRouter()
router.register(prefix="translations", viewset=TranslationViewSet)

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^$', TemplateView.as_view(template_name="translation/index.html") ),
)
